import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error



data = pd.read_excel("project1_used_car_data.xlsx")

x = data[
    [
        'Technical_Score',
        'Accident_Count',
        'Engine_L',
        'Mileage_km',
        'Year'
    ]
]

y = data['Price_USD']



x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.3,
    random_state=42
)

model = LinearRegression()

model.fit(x_train, y_train)



y_pred = model.predict(x_test)

MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)



BG = "#0f1117"
CARD = "#181c25"
INPUT = "#222733"

TEXT = "#f5f7fa"
MUTED = "#929bad"

ACCENT = "#5865f2"
ACCENT_HOVER = "#4752c4"

GREEN = "#43d17a"


root = tk.Tk()

root.title("Car Price Predictor")
root.geometry("720x700")
root.resizable(False, False)
root.configure(bg=BG)


page1 = tk.Frame(root, bg=BG)

page1.pack(fill="both", expand=True)


header = tk.Frame(page1, bg=BG)

header.pack(
    fill="x",
    padx=55,
    pady=(35, 15)
)


title = tk.Label(
    header,
    text="🚗  Car Price Predictor",
    font=("Segoe UI", 26, "bold"),
    fg=TEXT,
    bg=BG
)

title.pack(anchor="w")


subtitle = tk.Label(
    header,
    text="Enter the vehicle information to predict its price",
    font=("Segoe UI", 11),
    fg=MUTED,
    bg=BG
)

subtitle.pack(
    anchor="w",
    pady=(6, 0)
)



card = tk.Frame(
    page1,
    bg=CARD,
    highlightthickness=1,
    highlightbackground="#2a303d"
)

card.pack(
    fill="both",
    expand=True,
    padx=55,
    pady=15
)


entries = {}



def create_input(
    name,
    description,
    row
):

    label = tk.Label(
        card,
        text=name,
        font=("Segoe UI", 11, "bold"),
        fg=TEXT,
        bg=CARD
    )

    label.grid(
        row=row,
        column=0,
        sticky="w",
        padx=(30, 15),
        pady=(15, 2)
    )


    desc = tk.Label(
        card,
        text=description,
        font=("Segoe UI", 9),
        fg=MUTED,
        bg=CARD
    )

    desc.grid(
        row=row + 1,
        column=0,
        sticky="w",
        padx=(30, 15),
        pady=(0, 8)
    )


    entry = tk.Entry(
        card,
        font=("Segoe UI", 11),
        bg=INPUT,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        bd=0
    )

    entry.grid(
        row=row,
        column=1,
        rowspan=2,
        sticky="ew",
        padx=(10, 30),
        pady=(15, 8),
        ipady=9
    )

    entries[name] = entry

create_input(
    "Mileage_km",
    "Total distance driven in kilometers",
    0
)

create_input(
    "Engine_L",
    "Engine size in liters (Example: 1.6)",
    2
)

create_input(
    "Accident_Count",
    "Number of accidents (Example: 0)",
    4
)

create_input(
    "Technical_Score",
    "Technical condition score (Example: 8.5)",
    6
)

create_input(
    "Year",
    "Manufacturing year (Example: 2022)",
    8
)


card.grid_columnconfigure(
    0,
    weight=1
)

card.grid_columnconfigure(
    1,
    weight=1
)



def predict_price():

    try:

        mileage = float(
            entries["Mileage_km"].get()
        )

        engine = float(
            entries["Engine_L"].get()
        )

        accidents = int(
            entries["Accident_Count"].get()
        )

        technical = float(
            entries["Technical_Score"].get()
        )

        year = int(
            entries["Year"].get()
        )


  

        input_data = pd.DataFrame(
            [[
                technical,
                accidents,
                engine,
                mileage,
                year
            ]],
            columns=[
                'Technical_Score',
                'Accident_Count',
                'Engine_L',
                'Mileage_km',
                'Year'
            ]
        )


        # ---------------------------------------------

        prediction = model.predict(
            input_data
        )[0]




        show_result_page(
            prediction,
            mileage,
            engine,
            accidents,
            technical,
            year
        )


    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers in all fields."
        )




predict_button = tk.Button(
    card,
    text="Predict Price  →",
    command=predict_price,
    font=("Segoe UI", 12, "bold"),
    fg="white",
    bg=ACCENT,
    activeforeground="white",
    activebackground=ACCENT_HOVER,
    relief="flat",
    bd=0,
    cursor="hand2"
)

predict_button.grid(
    row=10,
    column=0,
    columnspan=2,
    sticky="ew",
    padx=30,
    pady=(20, 25),
    ipady=12
)



page2 = tk.Frame(
    root,
    bg=BG
)


def show_result_page(
    prediction,
    mileage,
    engine,
    accidents,
    technical,
    year
):

    page1.pack_forget()
    page2.pack(
        fill="both",
        expand=True
    )


  
    for widget in page2.winfo_children():
        widget.destroy()




    tk.Label(
        page2,
        text="📊  Prediction Result",
        font=("Segoe UI", 26, "bold"),
        fg=TEXT,
        bg=BG
    ).pack(
        anchor="w",
        padx=55,
        pady=(40, 5)
    )


    tk.Label(
        page2,
        text="Your vehicle's estimated market price",
        font=("Segoe UI", 11),
        fg=MUTED,
        bg=BG
    ).pack(
        anchor="w",
        padx=55
    )


    price_card = tk.Frame(
        page2,
        bg=CARD,
        highlightthickness=1,
        highlightbackground="#2a303d"
    )

    price_card.pack(
        fill="x",
        padx=55,
        pady=(25, 15)
    )


    tk.Label(
        price_card,
        text="Estimated Price",
        font=("Segoe UI", 11),
        fg=MUTED,
        bg=CARD
    ).pack(
        pady=(20, 5)
    )


    tk.Label(
        price_card,
        text=f"${prediction:,.2f}",
        font=("Segoe UI", 32, "bold"),
        fg=GREEN,
        bg=CARD
    ).pack(
        pady=(0, 20)
    )



    tk.Label(
        page2,
        text="Model Performance",
        font=("Segoe UI", 15, "bold"),
        fg=TEXT,
        bg=BG
    ).pack(
        anchor="w",
        padx=55,
        pady=(15, 10)
    )


    metrics = tk.Frame(
        page2,
        bg=BG
    )

    metrics.pack(
        fill="x",
        padx=55
    )



    mae_card = tk.Frame(
        metrics,
        bg=CARD
    )

    mae_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 7)
    )


    tk.Label(
        mae_card,
        text="MAE",
        font=("Segoe UI", 11, "bold"),
        fg=MUTED,
        bg=CARD
    ).pack(
        pady=(15, 5)
    )


    tk.Label(
        mae_card,
        text=f"${MAE:,.2f}",
        font=("Segoe UI", 16, "bold"),
        fg=TEXT,
        bg=CARD
    ).pack(
        pady=(0, 15)
    )


    mse_card = tk.Frame(
        metrics,
        bg=CARD
    )

    mse_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=7
    )


    tk.Label(
        mse_card,
        text="MSE",
        font=("Segoe UI", 11, "bold"),
        fg=MUTED,
        bg=CARD
    ).pack(
        pady=(15, 5)
    )


    tk.Label(
        mse_card,
        text=f"{MSE:,.2f}",
        font=("Segoe UI", 16, "bold"),
        fg=TEXT,
        bg=CARD
    ).pack(
        pady=(0, 15)
    )



    rmse_card = tk.Frame(
        metrics,
        bg=CARD
    )

    rmse_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(7, 0)
    )


    tk.Label(
        rmse_card,
        text="RMSE",
        font=("Segoe UI", 11, "bold"),
        fg=MUTED,
        bg=CARD
    ).pack(
        pady=(15, 5)
    )


    tk.Label(
        rmse_card,
        text=f"${RMSE:,.2f}",
        font=("Segoe UI", 16, "bold"),
        fg=TEXT,
        bg=CARD
    ).pack(
        pady=(0, 15)
    )



    summary = tk.Frame(
        page2,
        bg=CARD
    )

    summary.pack(
        fill="x",
        padx=55,
        pady=25
    )


    tk.Label(
        summary,
        text="Vehicle Information",
        font=("Segoe UI", 12, "bold"),
        fg=TEXT,
        bg=CARD
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )


    info = (
        f"Mileage       {mileage:,.0f} km     •     "
        f"Engine       {engine} L\n\n"
        f"Accidents     {accidents}             •     "
        f"Technical Score       {technical}\n\n"
        f"Year          {year}"
    )


    tk.Label(
        summary,
        text=info,
        font=("Segoe UI", 10),
        fg=MUTED,
        bg=CARD,
        justify="left"
    ).pack(
        anchor="w",
        padx=20,
        pady=(0, 15)
    )



    tk.Button(
        page2,
        text="←  Back",
        command=back_to_input,
        font=("Segoe UI", 11, "bold"),
        fg=TEXT,
        bg=INPUT,
        activeforeground=TEXT,
        activebackground="#2a3040",
        relief="flat",
        bd=0,
        cursor="hand2"
    ).pack(
        padx=55,
        fill="x",
        ipady=10
    )


def back_to_input():

    page2.pack_forget()

    page1.pack(
        fill="both",
        expand=True
    )



root.mainloop()