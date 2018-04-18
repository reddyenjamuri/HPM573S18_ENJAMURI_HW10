import HW9.ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClass as PathCls
import scr.FigureSupport as Figs


# look at outcomes for both non-treatment (mono) and treatment (anticoagulation) scenarios



# create a cohort1 for mono therapy
cohort1 = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.MONO)
# simulate the cohort
simOutputs1 = cohort1.simulate()


# create a cohort2 for anticoagulation therapy
cohort2 = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)
# simulate the cohort
simOutputs2 = cohort2.simulate()




# problem 1- print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs1, 'No treatment scenario:')
SupportMarkov.print_outcomes(simOutputs2, 'Treatment scenario:')

# problem 2- expected increase in total costs and total utilities
SupportMarkov.print_comparative_outcomes(simOutputs1, simOutputs2)

#problem 3- cost benefit analysis
SupportMarkov.report_CEA_CBA(simOutputs1, simOutputs2)
