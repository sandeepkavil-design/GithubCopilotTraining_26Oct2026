/* Host-side mock HAL implementation (SIL). See mock_hal.h. */
#include "mock_hal.h"

#include <string.h>

#define MOCK_ADC_CHANNELS  8U
#define MOCK_NVM_SIZE      1024U

static uint32_t s_now_ms;

typedef struct {
    MockSample_t   samples[MOCK_MAX_SAMPLES];
    uint8_t        count;
    MockAdcFault_t fault;
} AdcChannel_t;

static AdcChannel_t    s_adc[MOCK_ADC_CHANNELS];
static MockPwmRecord_t s_pwm[MOCK_MAX_RECORDS];
static uint16_t        s_pwm_count;
static uint8_t         s_nvm[MOCK_NVM_SIZE];
static bool            s_nvm_fail_next;
static uint32_t        s_wdg_kicks;

/* ---- time ---- */
void MockTime_Reset(void) { s_now_ms = 0U; }
void MockTime_Advance(uint32_t delta_ms) { s_now_ms += delta_ms; }
uint32_t Hal_GetTimeMs(void) { return s_now_ms; }

/* ---- ADC ---- */
void MockAdc_Reset(void) { (void)memset(s_adc, 0, sizeof(s_adc)); }

void MockAdc_Load(uint8_t channel, const MockSample_t *samples, uint8_t count)
{
    if ((channel < MOCK_ADC_CHANNELS) && (samples != NULL) && (count <= MOCK_MAX_SAMPLES)) {
        (void)memcpy(s_adc[channel].samples, samples, (size_t)count * sizeof(MockSample_t));
        s_adc[channel].count = count;
    }
}

void MockAdc_InjectFault(uint8_t channel, MockAdcFault_t fault)
{
    if (channel < MOCK_ADC_CHANNELS) {
        s_adc[channel].fault = fault;
    }
}

bool Hal_AdcRead(uint8_t channel, uint16_t *raw, uint32_t *age_ms)
{
    bool ok = false;
    if ((channel < MOCK_ADC_CHANNELS) && (raw != NULL) && (age_ms != NULL)) {
        const AdcChannel_t *ch = &s_adc[channel];
        if ((ch->fault != MOCK_ADC_DISCONNECTED) && (ch->count > 0U)) {
            uint8_t idx = 0U;
            for (uint8_t i = 0U; i < ch->count; i++) {
                if (ch->samples[i].t_ms <= s_now_ms) {
                    idx = i;
                }
            }
            *raw = ch->samples[idx].raw;
            *age_ms = (ch->fault == MOCK_ADC_STALE) ? 0xFFFFU : (s_now_ms - ch->samples[idx].t_ms);
            ok = true;
        }
    }
    return ok;
}

/* ---- PWM ---- */
void MockPwm_Reset(void) { s_pwm_count = 0U; }

void Hal_PwmSet(uint16_t duty_permille, bool enable)
{
    if (s_pwm_count < MOCK_MAX_RECORDS) {
        s_pwm[s_pwm_count].t_ms = s_now_ms;
        s_pwm[s_pwm_count].duty_permille = duty_permille;
        s_pwm[s_pwm_count].enable = enable;
        s_pwm_count++;
    }
}

uint16_t MockPwm_Count(void) { return s_pwm_count; }

const MockPwmRecord_t *MockPwm_Get(uint16_t index)
{
    return (index < s_pwm_count) ? &s_pwm[index] : NULL;
}

/* ---- NVM ---- */
void MockNvm_Reset(void)
{
    (void)memset(s_nvm, 0xFF, sizeof(s_nvm));
    s_nvm_fail_next = false;
}

bool Hal_NvmRead(uint16_t addr, uint8_t *dst, uint16_t len)
{
    bool ok = false;
    if ((dst != NULL) && ((uint32_t)addr + len <= MOCK_NVM_SIZE)) {
        (void)memcpy(dst, &s_nvm[addr], len);
        ok = true;
    }
    return ok;
}

bool Hal_NvmWrite(uint16_t addr, const uint8_t *src, uint16_t len)
{
    bool ok = false;
    if (s_nvm_fail_next) {
        s_nvm_fail_next = false;
    } else if ((src != NULL) && ((uint32_t)addr + len <= MOCK_NVM_SIZE)) {
        (void)memcpy(&s_nvm[addr], src, len);
        ok = true;
    }
    return ok;
}

void MockNvm_Corrupt(uint16_t addr)
{
    if (addr < MOCK_NVM_SIZE) {
        s_nvm[addr] ^= 0xFFU;
    }
}

void MockNvm_FailNextWrite(void) { s_nvm_fail_next = true; }

/* ---- watchdog ---- */
void MockWdg_Reset(void) { s_wdg_kicks = 0U; }
void Hal_WdgKick(void) { s_wdg_kicks++; }
uint32_t MockWdg_KickCount(void) { return s_wdg_kicks; }
