from pathlib import Path
import pandas as pd
import joblib
from tkinter import *
import tkinter as tk
from customtkinter import *
from PIL import Image

rf = joblib.load('model.pkl')

#button slide1
def left():
    image22 = CTkImage(light_image=Image.open("assets/slide1_img.png"), size=(445, 228))
    label.configure(image=image22)


#button slide2
def center():
    image22 = CTkImage(light_image=Image.open("assets/slide2_img.png"), size=(445, 228))
    label.configure(image=image22)


#button slide3
def right():
    image22 = CTkImage(light_image=Image.open("assets/slide3_img.png"), size=(445, 228))
    label.configure(image=image22)


def predict():
    if entry_spanok.get() == '':
        print("entry_spanok = null")
        return
    if entry_vaha.get() == '':
        print("entry_vaha = null")
        return
    if entry_vyska.get() == '':
        print("entry_vyska = null")
        return

    age_cat = 0
    age_cat_get = int(entry_age.get())

    if age_cat_get < 18:
        print("Age must be > 18")
        return
    elif age_cat_get >= 25 & age_cat_get <= 29:
        age_cat = 1
    elif age_cat_get >= 30 & age_cat_get <= 34:
        age_cat = 2
    elif age_cat_get >= 35 & age_cat_get <= 39:
        age_cat = 3
    elif age_cat_get >= 40 & age_cat_get <= 44:
        age_cat = 4
    elif age_cat_get >= 45 & age_cat_get <= 49:
        age_cat = 5
    elif age_cat_get >= 50 & age_cat_get <= 54:
        age_cat = 6
    elif age_cat_get >= 55 & age_cat_get <= 59:
        age_cat = 7
    elif age_cat_get >= 60 & age_cat_get <= 64:
        age_cat = 8
    elif age_cat_get >= 65 & age_cat_get <= 69:
        age_cat = 9
    elif age_cat_get >= 70 & age_cat_get <= 74:
        age_cat = 10
    elif age_cat_get >= 75 & age_cat_get <= 79:
        age_cat = 11
    elif age_cat_get >= 80 & age_cat_get <= 84:
        age_cat = 12
    elif age_cat_get >= 85:
        age_cat = 13

    smoker_status = 1
    if smoker_status_combobox.get() == "Never":
        smoker_status = 1
    elif smoker_status_combobox.get() == "Former":
        smoker_status = 2
    elif smoker_status_combobox.get() == "Current":
        smoker_status = 3

    cigarette_status = 1
    if ecigarette_status_combobox.get() == "Never":
        cigarette_status = 1
    elif ecigarette_status_combobox.get() == "Former":
        cigarette_status = 2
    elif ecigarette_status_combobox.get() == "Current":
        cigarette_status = 3

    general_health_status = 0
    if general_health_status_combobox.get() == "Poor":
        general_health_status = 0
    elif general_health_status_combobox.get() == "Fair":
        general_health_status = 1
    elif general_health_status_combobox.get() == "Good":
        general_health_status = 2
    elif general_health_status_combobox.get() == "Very good":
        general_health_status = 3
    elif general_health_status_combobox.get() == "Excellent":
        general_health_status = 4

    LastCheckupTime_cat =0
    if LastCheckupTime_combobox.get() == "Within past year":
        LastCheckupTime_cat = 0
    elif LastCheckupTime_combobox.get() == "Within past 2 years":
        LastCheckupTime_cat = 1
    elif LastCheckupTime_combobox.get() == "Within past 5 years":
        LastCheckupTime_cat = 2
    elif LastCheckupTime_combobox.get() == "5 or more years ago":
        LastCheckupTime_cat = 3

    user_input = {
        'Sex': v_pohlavie.get(),
        'GeneralHealth': general_health_status,
        'PhysicalHealthDays': int(physical_health_days.get()),
        'MentalHealthDays': int(mental_health_days.get()),
        'LastCheckupTime': LastCheckupTime_cat,
        'PhysicalActivities': cb_PhysicalActivities.get(),
        'SleepHours': int(entry_spanok.get()),
        'RemovedTeeth': 1 if v_RemovedTeeth.get() == 0 else 0,
        'HadAngina': cb_HadAngina.get(),
        'HadStroke': cb_HadStroke.get(),
        'HadCOPD': cb_HadCOPD.get(),
        'HadKidneyDisease': cb_HadKidneyDisease.get(),
        'HadArthritis': cb_HadArthritis.get(),
        'HadDiabetes': cb_HadDiabetes.get(),
        'DeafOrHardOfHearing': cb_FluVaxLast12.get(),
        'BlindOrVisionDifficulty': cb_CovidPos.get(),
        'DifficultyConcentrating': cb_DifficultyConcentrating.get(),
        'SmokerStatus': smoker_status,
        'ECigaretteUsage': cigarette_status,
        'ChestScan': cb_ChestScan.get(),
        'AgeCategory': age_cat,
        'HeightInMeters': float(entry_vyska.get()),
        'WeightInKilograms': float(entry_vaha.get()),
        'AlcoholDrinkers': cb_AlcoholDrinkers.get(),
        'HIVTesting': cb_HadDepressiveDisorder.get(),
        'PneumoVaxEver': cb_PneumoVaxEver.get(),
        'HighRiskLastYear': cb_HighRiskLastYear.get(),
        'DifficultyMobility': cb_DifficultyMobility.get(),
    }

    user_input_df = pd.DataFrame(user_input, index=[0])

    prediction = rf.predict(user_input_df)
    res = "Ano"
    if prediction == 0:
        res = "Nie"
    result.configure(text=f"Pravdepodobnosť srdcového ochorenia: {res}")
    proba = rf.predict_proba(pd.DataFrame(user_input, index=[0]))
    print(f"Pravdepodobnosť predikcie: {proba[0][1] * 100:.2f}%")


window = Tk()
window.geometry("1000x783")
window.configure(bg="#F9FAFC")
window.title("Aplikácia prognózovania")
img = PhotoImage(file='assets/heartIco.png')
window.iconphoto(False, img)

canvas = Canvas(
    window,
    bg="#F9FAFC",
    height=783,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=("assets/background_img.png"))
image_1 = canvas.create_image(
    500.0,
    391.5,
    image=image_image_1
)
text_var = "Pravdepodobnosť srdcového ochorenia: ---"

result = CTkLabel(master=window,
                  text=text_var, bg_color="white", text_color="black", font=("Roboto", 16)
                  )
result.place(x=85, y=675)


#region Label
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Zdravie srdca",
                 font=("Roboto medium", 24),
                 )
label_t.place(x=190,
            y=47)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="srdcového ochorenia.",
                 font=("Roboto light", 15)
                 )
label_t.place(x=40,
            y=316)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Aplikácia využíva zdravotné údaje pacienta na odhad rizika",
                 font=("Roboto light", 15)
                 )
label_t.place(x=40,
            y=297)

label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Hlavné faktory srdcového ochorenia:",
                 font=("Roboto medium", 18)
                 )
label_t.place(x=40,
            y=355)

#title
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Osobné údaje",
                 font=("Roboto medium", 18)
                 )
label_t.place(x=525,
            y=50)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Anamnéza",
                 font=("Roboto medium", 18)
                 )
label_t.place(x=525,
            y=239)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Zdravie a životný štýl",
                 font=("Roboto medium", 18)
                 )
label_t.place(x=525,
            y=349)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Chronické ochorenia",
                 font=("Roboto medium", 18)
                 )
label_t.place(x=525,
            y=584)

#small t
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Váha:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=525,
            y=75)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Výška:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=745,
            y=75)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Veková kategória:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=525,
            y=126)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Pohlavie:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=525,
            y=178)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Dni fyzického zdravia:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=525,
            y=372)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Dni duševného zdravia:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=745,
            y=372)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Fajčiarsky status:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=525,
            y=423)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Používanie e-cigariet:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=745,
            y=423)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Všeobecný zdravotný stav:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=525,
            y=474)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Počet hodín spánku:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=525,
            y=525)

label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Odstránenie zubov:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=745,
            y=474)
label_t = CTkLabel(master=window,
                 text_color="black",
                 bg_color="white",
                 text="Čas posledného vyšetrenia:",
                 font=("Roboto lite", 14)
                 )
label_t.place(x=745,
            y=525)

# Osobné údaje
entry_vaha = CTkEntry(master=window,
                      placeholder_text="74",
                      bg_color="#FFFFFF",
                      fg_color="#FFFFFF",
                      text_color="#000000",
                      corner_radius=5,
                      border_width=1,
                      border_color="#D9DFEB",

                      width=205,
                      height=25
                      )

entry_vaha.place(
    x=525.0,
    y=99.0
)
entry_vyska = CTkEntry(master=window,
                       placeholder_text="1.8",
                       bg_color="#FFFFFF",
                       fg_color="#FFFFFF",
                       text_color="#000000",
                       corner_radius=5,
                       border_width=1,
                       border_color="#D9DFEB",
                       width=205,
                       height=25
                       )

entry_vyska.place(
    x=745.0,
    y=99.0
)
entry_age = CTkEntry(master=window,
                       placeholder_text="30",
                       bg_color="#FFFFFF",
                       fg_color="#FFFFFF",
                       text_color="#000000",
                       corner_radius=5,
                       border_width=1,
                       border_color="#D9DFEB",
                       width=205,
                       height=25
                       )

entry_age.place(
    x=525.0,
    y=150.0
)
v_pohlavie = tk.IntVar()
rb_pohlavie_men = CTkRadioButton(master=window,
                                 text="Muž",
                                 bg_color="#FFFFFF",
                                 fg_color="red",
                                 text_color="#000000",
                                 border_color="#D9DFEB",
                                 hover_color="#D13200",
                                 value=0,
                                 border_width_checked=4,
                                 variable=v_pohlavie,
                                 radiobutton_width=15,
                                 radiobutton_height=15
                                 )

rb_pohlavie_men.place(
    x=525.0,
    y=204.0
)
rb_pohlavie_women = CTkRadioButton(master=window,
                                   text="Žena",
                                   bg_color="#FFFFFF",
                                   fg_color="red",
                                   text_color="#000000",
                                   border_color="#D9DFEB",
                                   hover_color="#D13200",
                                   value=1,
                                   border_width_checked=4,
                                   variable=v_pohlavie,
                                   radiobutton_width=15,
                                   radiobutton_height=15
                                   )

rb_pohlavie_women.place(
    x=575.0,
    y=204.0
)

# Anamneza
cb_AlcoholDrinkers = CTkCheckBox(master=window,
                                 text="Alcohol drinkers",
                                 bg_color="#FFFFFF",
                                 fg_color="red",
                                 text_color="#000000",
                                 border_color="#D9DFEB",
                                 hover_color="#D13200",
                                 border_width=1,
                                 corner_radius=0,
                                 checkbox_width=15,
                                 checkbox_height=15,
                                 width=15,
                                 height=15
                                 )
cb_AlcoholDrinkers.place(
    x=525.0,
    y=268.0
)
cb_FluVaxLast12 = CTkCheckBox(master=window,
                              text="Hard of hearing",
                              bg_color="#FFFFFF",
                              fg_color="red",
                              text_color="#000000",
                              border_color="#D9DFEB",
                              hover_color="#D13200",
                              border_width=1,
                              corner_radius=0,
                              checkbox_width=15,
                              checkbox_height=15,
                              width=15,
                              height=15
                              )
cb_FluVaxLast12.place(
    x=525.0,
    y=291.0
)

cb_PneumoVaxEver = CTkCheckBox(master=window,
                               text="PneumoVax",
                               bg_color="#FFFFFF",
                               fg_color="red",
                               text_color="#000000",
                               border_color="#D9DFEB",
                               hover_color="#D13200",
                               border_width=1,
                               corner_radius=0,
                               checkbox_width=15,
                               checkbox_height=15,
                               width=15,
                               height=15
                               )
cb_PneumoVaxEver.place(
    x=525.0,
    y=314.0
)
cb_HighRiskLastYear = CTkCheckBox(master=window,
                                  text="High risk last year",
                                  bg_color="#FFFFFF",
                                  fg_color="red",
                                  text_color="#000000",
                                  border_color="#D9DFEB",
                                  hover_color="#D13200",
                                  border_width=1,
                                  corner_radius=0,
                                  checkbox_width=15,
                                  checkbox_height=15,
                                  width=15,
                                  height=15
                                  )
cb_HighRiskLastYear.place(
    x=655.0,
    y=268.0
)
cb_CovidPos = CTkCheckBox(master=window,
                          text="Vision Difficulty",
                          bg_color="#FFFFFF",
                          fg_color="red",
                          text_color="#000000",
                          border_color="#D9DFEB",
                          hover_color="#D13200",
                          border_width=1,
                          corner_radius=0,
                          checkbox_width=15,
                          checkbox_height=15,
                          width=15,
                          height=15
                          )
cb_CovidPos.place(
    x=655.0,
    y=291.0
)

cb_DifficultyMobility = CTkCheckBox(master=window,
                                    text="Difficulty mobility",
                                    bg_color="#FFFFFF",
                                    fg_color="red",
                                    text_color="#000000",
                                    border_color="#D9DFEB",
                                    hover_color="#D13200",
                                    border_width=1,
                                    corner_radius=0,
                                    checkbox_width=15,
                                    checkbox_height=15,
                                    width=15,
                                    height=15
                                    )
cb_DifficultyMobility.place(
    x=655.0,
    y=314.0
)
cb_DifficultyConcentrating = CTkCheckBox(master=window,
                                         text="Difficulty concentrating",
                                         bg_color="#FFFFFF",
                                         fg_color="red",
                                         text_color="#000000",
                                         border_color="#D9DFEB",
                                         hover_color="#D13200",
                                         border_width=1,
                                         corner_radius=0,
                                         checkbox_width=15,
                                         checkbox_height=15,
                                         width=15,
                                         height=15
                                         )
cb_DifficultyConcentrating.place(
    x=795.0,
    y=268.0
)
cb_ChestScan = CTkCheckBox(master=window,
                           text="Chest scan",
                           bg_color="#FFFFFF",
                           fg_color="red",
                           text_color="#000000",
                           border_color="#D9DFEB",
                           hover_color="#D13200",
                           border_width=1,
                           corner_radius=0,
                           checkbox_width=15,
                           checkbox_height=15,
                           width=15,
                           height=15
                           )
cb_ChestScan.place(
    x=795.0,
    y=291.0
)

cb_PhysicalActivities = CTkCheckBox(master=window,
                                    text="Physical activities",
                                    bg_color="#FFFFFF",
                                    fg_color="red",
                                    text_color="#000000",
                                    border_color="#D9DFEB",
                                    hover_color="#D13200",
                                    border_width=1,
                                    corner_radius=0,
                                    checkbox_width=15,
                                    checkbox_height=15,
                                    width=15,
                                    height=15
                                    )
cb_PhysicalActivities.place(
    x=795.0,
    y=314.0
)

# Zdravie a životný štýl
mental_health_days = CTkEntry(master=window,
                      placeholder_text="20",
                      bg_color="#FFFFFF",
                      fg_color="#FFFFFF",
                      text_color="#000000",
                      corner_radius=5,
                      border_width=1,
                      border_color="#D9DFEB",

                      width=205,
                      height=25
                      )

mental_health_days.place(
    x=525.0,
    y=396.0
)

physical_health_days = CTkEntry(master=window,
                      placeholder_text="20",
                      bg_color="#FFFFFF",
                      fg_color="#FFFFFF",
                      text_color="#000000",
                      corner_radius=5,
                      border_width=1,
                      border_color="#D9DFEB",

                      width=205,
                      height=25
                      )

physical_health_days.place(
    x=745.0,
    y=396.0
)

smoker_status_combobox = CTkComboBox(master=window,
                                          values=["Never", "Former", "Current"],
                                          bg_color="#FFFFFF",
                                          fg_color="#FFFFFF",
                                          dropdown_fg_color="#FFFFFF",
                                          button_color="#D9DFEB",
                                          dropdown_text_color="#000000",
                                          dropdown_hover_color="#D9DFEB",
                                          text_color="#000000",
                                          border_color="#D9DFEB",
                                          corner_radius=5,
                                          border_width=1,
                                          width=205,
                                          height=25
                                          )

smoker_status_combobox.place(
    x=525.0,
    y=449.0
)

ecigarette_status_combobox = CTkComboBox(master=window,
                                          values=["Never", "Former", "Current"],
                                          bg_color="#FFFFFF",
                                          fg_color="#FFFFFF",
                                          dropdown_fg_color="#FFFFFF",
                                          button_color="#D9DFEB",
                                          dropdown_text_color="#000000",
                                          dropdown_hover_color="#D9DFEB",
                                          text_color="#000000",
                                          border_color="#D9DFEB",
                                          corner_radius=5,
                                          border_width=1,
                                          width=205,
                                          height=25
                                          )

ecigarette_status_combobox.place(
    x=745.0,
    y=449.0
)

general_health_status_combobox = CTkComboBox(master=window,
                                      values=["Poor", "Fair", "Good", "Excellent"],
                                      bg_color="#FFFFFF",
                                      fg_color="#FFFFFF",
                                      dropdown_fg_color="#FFFFFF",
                                      button_color="#D9DFEB",
                                      dropdown_text_color="#000000",
                                      dropdown_hover_color="#D9DFEB",
                                      text_color="#000000",
                                      border_color="#D9DFEB",
                                      corner_radius=5,
                                      border_width=1,
                                      width=205,
                                      height=25
                                      )

general_health_status_combobox.place(
    x=525.0,
    y=498.0
)

entry_spanok = CTkEntry(master=window,
                        placeholder_text="8",
                        bg_color="#FFFFFF",
                        fg_color="#FFFFFF",
                        text_color="#000000",
                        corner_radius=5,
                        border_width=1,
                        border_color="#D9DFEB",
                        width=205,
                        height=25
                        )

entry_spanok.place(
    x=525.0,
    y=549.0
)

v_RemovedTeeth = tk.IntVar()
rb_RemovedTeeth_ano = CTkRadioButton(master=window,
                                   text="Ano",
                                   bg_color="#FFFFFF",
                                   fg_color="red",
                                   text_color="#000000",
                                   border_color="#D9DFEB",
                                   hover_color="#D13200",
                                   value=1,
                                   border_width_checked=4,
                                   variable=v_RemovedTeeth,
                                   radiobutton_width=15,
                                   radiobutton_height=15
                                   )

rb_RemovedTeeth_ano.place(
    x=745.0,
    y=498.0
)
rb_RemovedTeeth_nie = CTkRadioButton(master=window,
                                   text="Nie",
                                   bg_color="#FFFFFF",
                                   fg_color="red",
                                   text_color="#000000",
                                   border_color="#D9DFEB",
                                   hover_color="#D13200",
                                   value=0,
                                   border_width_checked=4,
                                   variable=v_RemovedTeeth,
                                   radiobutton_width=15,
                                   radiobutton_height=15
                                   )

rb_RemovedTeeth_nie.place(
    x=795.0,
    y=498.0
)

LastCheckupTime_combobox = CTkComboBox(master=window,
                                          values=["Within past year", "Within past 2 years", "Within past 5 years", "5 or more years ago"],
                                          bg_color="#FFFFFF",
                                          fg_color="#FFFFFF",
                                          dropdown_fg_color="#FFFFFF",
                                          button_color="#D9DFEB",
                                          dropdown_text_color="#000000",
                                          dropdown_hover_color="#D9DFEB",
                                          text_color="#000000",
                                          border_color="#D9DFEB",
                                          corner_radius=5,
                                          border_width=1,
                                          width=205,
                                          height=25
                                          )

LastCheckupTime_combobox.place(
    x=745.0,
    y=549.0
)


# Chronické ochorenia
cb_HadAngina = CTkCheckBox(master=window,
                           text="Had angina",
                           bg_color="#FFFFFF",
                           fg_color="red",
                           text_color="#000000",
                           border_color="#D9DFEB",
                           hover_color="#D13200",
                           border_width=1,
                           corner_radius=0,
                           checkbox_width=15,
                           checkbox_height=15,
                           width=15,
                           height=15
                           )
cb_HadAngina.place(
    x=525.0,
    y=615.0
)
cb_HadArthritis = CTkCheckBox(master=window,
                              text="Had arthritis",
                              bg_color="#FFFFFF",
                              fg_color="red",
                              text_color="#000000",
                              border_color="#D9DFEB",
                              hover_color="#D13200",
                              border_width=1,
                              corner_radius=0,
                              checkbox_width=15,
                              checkbox_height=15,
                              width=15,
                              height=15
                              )
cb_HadArthritis.place(
    x=525.0,
    y=638.0
)

cb_HadCOPD = CTkCheckBox(master=window,
                         text="Had COPD",
                         bg_color="#FFFFFF",
                         fg_color="red",
                         text_color="#000000",
                         border_color="#D9DFEB",
                         hover_color="#D13200",
                         border_width=1,
                         corner_radius=0,
                         checkbox_width=15,
                         checkbox_height=15,
                         width=15,
                         height=15
                         )
cb_HadCOPD.place(
    x=525.0,
    y=661.0
)
cb_HadDepressiveDisorder = CTkCheckBox(master=window,
                                       text="HIVTesting",
                                       bg_color="#FFFFFF",
                                       fg_color="red",
                                       text_color="#000000",
                                       border_color="#D9DFEB",
                                       hover_color="#D13200",
                                       border_width=1,
                                       corner_radius=0,
                                       checkbox_width=15,
                                       checkbox_height=15,
                                       width=15,
                                       height=15
                                       )
cb_HadDepressiveDisorder.place(
    x=795.0,
    y=615.0
)
cb_HadDiabetes = CTkCheckBox(master=window,
                             text="Had diabetes",
                             bg_color="#FFFFFF",
                             fg_color="red",
                             text_color="#000000",
                             border_color="#D9DFEB",
                             hover_color="#D13200",
                             border_width=1,
                             corner_radius=0,
                             checkbox_width=15,
                             checkbox_height=15,
                             width=15,
                             height=15
                             )
cb_HadDiabetes.place(
    x=655.0,
    y=638.0
)

cb_HadKidneyDisease = CTkCheckBox(master=window,
                                  text="Had kidney disease",
                                  bg_color="#FFFFFF",
                                  fg_color="red",
                                  text_color="#000000",
                                  border_color="#D9DFEB",
                                  hover_color="#D13200",
                                  border_width=1,
                                  corner_radius=0,
                                  checkbox_width=15,
                                  checkbox_height=15,
                                  width=15,
                                  height=15
                                  )
cb_HadKidneyDisease.place(
    x=795.0,
    y=638.0
)
cb_HadStroke = CTkCheckBox(master=window,
                           text="Had stroke",
                           bg_color="#FFFFFF",
                           fg_color="red",
                           text_color="#000000",
                           border_color="#D9DFEB",
                           hover_color="#D13200",
                           border_width=1,
                           corner_radius=0,
                           checkbox_width=15,
                           checkbox_height=15,
                           width=15,
                           height=15
                           )
cb_HadStroke.place(
    x=655.0,
    y=615.0
)

predict_button = CTkButton(master=window,
                           text="Rozpoznať riziko",
                           bg_color="#FFFFFF",
                           fg_color="#e73f0b",
                           text_color="#FFFFFF",
                           hover_color="#D13200",
                           corner_radius=10,
                           font=("Roboto", 16),
                           width=205,
                           height=32,
                           command=predict
                           )
predict_button.place(
    x=635.0,
    y=701.0
)
vsw = tk.IntVar()

left_button = CTkRadioButton(master=window,
                               text="",
                               bg_color="#FFFFFF",
                               fg_color="red",
                               text_color="#000000",
                               border_color="#D9DFEB",
                               hover_color="#D13200",
                               value=0,
                               border_width_checked=3,
                               radiobutton_width=10,
                               radiobutton_height=10,
                               width=10,
                               height=10,
                               command=left,
                               variable=vsw
                               )
left_button.place(
    x=243.0,
    y=614.0
)
center_button = CTkRadioButton(master=window,
                             text="",
                             bg_color="#FFFFFF",
                             fg_color="red",
                             text_color="#000000",
                             border_color="#D9DFEB",
                             hover_color="#D13200",
                             value=1,
                             border_width_checked=3,
                             radiobutton_width=10,
                             radiobutton_height=10,
                             width=10,
                             height=10,
                             command=center,
                             variable=vsw
                             )
center_button.place(
    x=258.0,
    y=614.0
)
right_button = CTkRadioButton(master=window,
                              text="",
                              bg_color="#FFFFFF",
                              fg_color="red",
                              text_color="#000000",
                              border_color="#D9DFEB",
                              hover_color="#D13200",
                              value=2,
                              border_width_checked=3,
                              radiobutton_width=10,
                              radiobutton_height=10,
                              width=10,
                              height=10,
                              command=right,
                              variable=vsw
                              )
right_button.place(
    x=273.0,
    y=614.0
)


image22 = CTkImage(light_image=Image.open("assets/slide1_img.png"), size=(445, 228))
label = CTkLabel(master=window,
                 text="",
                 image=image22,
                 width=445,
                 height=228
                 )

label.place(x=30,
            y=386)

# window.resizable(False, False)
window.mainloop()
