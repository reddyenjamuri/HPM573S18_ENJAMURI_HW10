# Homework 7 simulation model followed a cohort of 573 individuals over 5 years
POP_SIZE = 573     # cohort population size
SIM_LENGTH = 5   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03     # annual discount rate

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,   0.0,    0.1],   # Well
    [0,     0.0,    1.0,    0.0],   # Stroke
    [0,     0.25,   0.55,   0.2],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0],   # Dead
    ]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0.0,    # Well
    5000.0, # Stroke
    200.0,  # Post-Stroke
    0.0     # Dead
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1.00,    # Well
    0.8865,  # Stroke
    0.90,    # Post-Stroke
    0.00,    # Dead
    ]

# annual drug costs
Anticoagulation_COST = 2000.0
NoTreatment_COST = 0.0

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05
