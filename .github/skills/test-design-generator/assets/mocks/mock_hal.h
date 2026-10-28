/* Host-side mock HAL skeleton for system/integration tests (SIL).
 * Replace the Hal_* names with the project's actual HAL interface.
 * TODO: CONFIRM_HAL_INTERFACE
 */
#ifndef MOCK_HAL_H
#define MOCK_HAL_H

#include <stdbool.h>
#include <stdint.h>

#define MOCK_MAX_SAMPLES   64U
#define MOCK_MAX_RECORDS   256U

/* ---- virtual time ---- */
void     MockTime_Reset(void);
void     MockTime_Advance(uint32_t delta_ms);
uint32_t Hal_GetTimeMs(void);

/* ---- scripted ADC input (sensors, dials, current sense) ---- */
typedef struct {
    uint32_t t_ms;
    uint16_t raw;
} MockSample_t;

typedef enum { MOCK_ADC_OK = 0, MOCK_ADC_STALE, MOCK_ADC_DISCONNECTED } MockAdcFault_t;

void     MockAdc_Reset(void);
void     MockAdc_Load(uint8_t channel, const MockSample_t *samples, uint8_t count);
void     MockAdc_InjectFault(uint8_t channel, MockAdcFault_t fault);
bool     Hal_AdcRead(uint8_t channel, uint16_t *raw, uint32_t *age_ms);

/* ---- recording PWM / motor driver output ---- */
typedef struct {
    uint32_t t_ms;
    uint16_t duty_permille;
    bool     enable;
} MockPwmRecord_t;

void                   MockPwm_Reset(void);
void                   Hal_PwmSet(uint16_t duty_permille, bool enable);
uint16_t               MockPwm_Count(void);
const MockPwmRecord_t *MockPwm_Get(uint16_t index);

/* ---- RAM-backed NVM with CRC corruption ---- */
void MockNvm_Reset(void);
bool Hal_NvmRead(uint16_t addr, uint8_t *dst, uint16_t len);
bool Hal_NvmWrite(uint16_t addr, const uint8_t *src, uint16_t len);
void MockNvm_Corrupt(uint16_t addr);
void MockNvm_FailNextWrite(void);

/* ---- watchdog ---- */
void     MockWdg_Reset(void);
void     Hal_WdgKick(void);
uint32_t MockWdg_KickCount(void);

#endif /* MOCK_HAL_H */
