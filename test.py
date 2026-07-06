from main import getCodes

test_notes = [
    {
        "patient_id": "TEST001",
        "note": """
        CC: fever, abd pain x3 days
        HPI: 34 yo M presents w/ high fever (up to 103F), diffuse abdominal
        pain, and rose-colored spots on trunk. Pt reports recent travel to
        rural area w/ poor water sanitaiton. Denies vomitting but c/o
        nausea and decreased appetite. Some loose stools past 2 days.
        PMH: none significant
        A/P: Clinical picture c/w typhoid fever, unspecified. Started on
        empiric abx pending blood cx results. Follow up in 48hrs.
        """
    },
    {
        "patient_id": "TEST002",
        "note": """
        Pt is a 58F w hx of HTN, T2DM presenting for f/u of chest pain.
        Pain described as pressure-like, substernal, radiating to left
        arm, worse w exertion, releived w rest. No SOB, no diaphoresis
        today. EKG obtained - shows nonspecific ST changes, no acute
        ischemic changes noted by cardiology.
        Plan: stress test ordered, contuining metoprolol, f/u 1wk
        """
    },
    {
        "patient_id": "TEST003",
        "note": """
        6 yo F brought in by mother for 2 days of profuse watery diarrhea,
        "rice water" appearance per mom. Child appears lethargic, dry
        mucous membranes, decreased urine output x24hrs. No recent travel
        but family recently returned from visiting relatives abroad.
        Assessment: Suspect cholera, unspecified. Started IV fluids
        aggresively, stool culture sent. Admtited for observation and
        rehydration.
        """
    },
    {
        "patient_id": "TEST004",
        "note": """
        45 yo male, construction worker, presents s/p fall from ladder
        approx 8ft ~2hrs ago. C/o severe R wrist pain, unable to bear
        weight or grip. Visible deformity noted. Denies LOC, denies
        head strike. Neurovascularly intact distally.
        Xray R wrist ordered - pending read.
        Plan: splint, ortho referal, ice/elevate, f/u after imaging
        """
    },
    {
        "patient_id": "TEST005",
        "note": """
        29F here for routine prenatal visit, currently 24 wks gestation.
        Reports mild swelling in ankles, otherwise feeling well. Fetal
        movement good per pt. No headaches, no visual changes, no
        contractions.
        BP slighty elevated today at 138/88 (baseline has been 118/74).
        Will recheck BP in 1 wk, sent for repeat labs incl urine protein
        to r/o preeclmpsia. Continue prenatal vitamins.
        """
    },
    {
        "patient_id": "TEST006",
        "note": """
        67 yo M w hx COPD presents w worsening SOB over past 4 days,
        increased sputum production, sputum now yellow-green (baseline
        clear). Using rescue inhaler more frequently w minimal relief.
        No fever. O2 sat 91% on RA, improved to 95% on 2L NC.
        Lungs w diffuse wheezes and dimished breath sounds bilat.
        A/P: COPD exacerbation, likely acute bronchitis superimposed.
        Started on prednisone taper + azithromycin, nebulizer tx given
        in office, f/u 3-5 days or sooner if worsening
        """
    },
    {
        "patient_id": "TEST007",
        "note": """
        22 yo F c/o sore throat, difficulty swallowing x 4 days, subjective
        fevers at home (didn't take temp). No cough. Tonsils erythematous
        w exudate bilaterally, tender anterior cervical lymphadenopathy.
        Rapid strep test: positive.
        Dx: Strep throat (streptococcal pharyngitis)
        Rx: Amoxicillin 500mg BID x10 days, supportive care, return if
        sx worsen or no improvment in 48-72hrs
        """
    }
]

def getMedicalInfo(n):
    itrs = min(len(test_notes), n)
    for i in range(itrs):
        yield test_notes[i]

def test1():
    for medical_info in getMedicalInfo(1):
        note = medical_info['note']
        ans = getCodes(f"{note}")
        print(f"Answer: {ans} - {note}")

def main():
    test1()

if __name__ == "__main__":
    main()

