import numpy as np
from django.shortcuts import render
import joblib

# Load the model
model = joblib.load("myApp/models/model.joblib")

def home(request):
    return render(request, "index.html")

def predict(request):
    if request.method == "POST":
        # Retrieve the form data from the POST request
        AlcoholicDrinkFrequency = float(request.POST.get('AlcoholicDrinkFrequency'))
        AvgAlcoholicDrinksPerDay = float(request.POST.get('AvgAlcoholicDrinksPerDay'))
        FourOrMoreDrinksDaily = float(request.POST.get('FourOrMoreDrinksDaily'))
        HighBloodPressureDiagnosis = float(request.POST.get('HighBloodPressureDiagnosis'))
        TakingHBP_Medication = float(request.POST.get('TakingHBP_Medication'))
        TakingCholesterol_Medication = float(request.POST.get('TakingCholesterol_Medication'))
        ChestPain = float(request.POST.get('ChestPain'))
        ChestPainHillHurry = float(request.POST.get('ChestPainHillHurry'))
        SevereChestPain = float(request.POST.get('SevereChestPain'))
        FastFoodFrequency = float(request.POST.get('FastFoodFrequency'))
        RestaurantMealFrequency = float(request.POST.get('RestaurantMealFrequency'))
        DailyCaloriesNeeded = float(request.POST.get('DailyCaloriesNeeded'))
        GlucoseMeasureUnit = float(request.POST.get('GlucoseMeasureUnit'))
        FeetSoresMeasureUnit = float(request.POST.get('FeetSoresMeasureUnit'))
        WholeMilkConsumption = float(request.POST.get('WholeMilkConsumption'))
        MealsNotHomePrepared = float(request.POST.get('MealsNotHomePrepared'))
        FastFoodMealsFrequency = float(request.POST.get('FastFoodMealsFrequency'))
        ReadyToEatFoodsFrequency = float(request.POST.get('ReadyToEatFoodsFrequency'))
        FrozenMealsFrequency = float(request.POST.get('FrozenMealsFrequency'))
        AsthmaDiagnosis = float(request.POST.get('AsthmaDiagnosis'))
        OverweightDiagnosis = float(request.POST.get('OverweightDiagnosis'))
        BloodTransfusion = float(request.POST.get('BloodTransfusion'))
        AbdominalPain = float(request.POST.get('AbdominalPain'))
        GallstonesDiagnosis = float(request.POST.get('GallstonesDiagnosis'))
        CancerDiagnosis = float(request.POST.get('CancerDiagnosis'))
        WeekdaySleepHours = float(request.POST.get('WeekdaySleepHours'))
        WeekendSleepHours = float(request.POST.get('WeekendSleepHours'))
        TroubleSleepingDiagnosis = float(request.POST.get('TroubleSleepingDiagnosis'))
        ExcessiveDaytimeSleepiness = float(request.POST.get('ExcessiveDaytimeSleepiness'))
        CigaretteMeasureUnit = float(request.POST.get('CigaretteMeasureUnit'))
        LifetimeCigaretteCount = float(request.POST.get('LifetimeCigaretteCount'))
        WeightPerception = float(request.POST.get('WeightPerception'))
        SuicidalThoughts = float(request.POST.get('SuicidalThoughts'))
        BMI = float(request.POST.get('BMI'))
        
        features = [AlcoholicDrinkFrequency, AvgAlcoholicDrinksPerDay, FourOrMoreDrinksDaily,
                    HighBloodPressureDiagnosis, TakingHBP_Medication, TakingCholesterol_Medication,
                    ChestPain, ChestPainHillHurry, SevereChestPain, FastFoodFrequency,
                    RestaurantMealFrequency, DailyCaloriesNeeded, GlucoseMeasureUnit,
                    FeetSoresMeasureUnit, WholeMilkConsumption, MealsNotHomePrepared,
                    FastFoodMealsFrequency, ReadyToEatFoodsFrequency, FrozenMealsFrequency,
                    AsthmaDiagnosis, OverweightDiagnosis, BloodTransfusion, AbdominalPain,
                    GallstonesDiagnosis, CancerDiagnosis, WeekdaySleepHours, WeekendSleepHours,
                    TroubleSleepingDiagnosis, ExcessiveDaytimeSleepiness, CigaretteMeasureUnit,
                    LifetimeCigaretteCount, WeightPerception, SuicidalThoughts, BMI]
        
        features = np.array([features])

        # Make predictions
        prediction = model.predict(features) 
        
        if prediction[0] == 1:
            pred = True
        elif prediction[0] == 2:
            pred = False

        return render(request, "index.html", {"prediction_text": f"Diabetes affected eyes/had retinopathy: {pred}"})

    return render(request, "index.html")
