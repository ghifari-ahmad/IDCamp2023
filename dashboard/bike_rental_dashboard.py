import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca data all_data.csv
merged_df = pd.read_csv('IDCamp2023/dashboard/all_data.csv')

# Sidebar
st.sidebar.title("Pilih Visualisasi")
visualization_choice = st.sidebar.radio("Visualisasi Data", ["Peminjaman per Musim", "Peminjaman per Cuaca", "Peminjaman per Hari", "Peminjaman per Hari Kerja", "Peminjaman per Hari Libur", "Peminjaman per Rentang Jam"])

# Main content
st.title("Dashboard Peminjaman Sepeda")

# Visualisasi data berdasarkan pilihan
if visualization_choice == "Peminjaman per Musim":
    # Visualisasi peminjaman per musim
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(x="season", y="cnt", data=merged_df.groupby("season")["cnt"].sum().reset_index())
    plt.title("Frekuensi Peminjaman Sepeda Berdasarkan Musim")
    plt.xlabel("Musim")
    plt.ylabel("Jumlah Peminjaman Sepeda")
    st.pyplot(fig)

elif visualization_choice == "Peminjaman per Cuaca":
    # Visualisasi peminjaman per cuaca
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(x="weathersit", y="cnt", data=merged_df.groupby("weathersit")["cnt"].sum().reset_index())
    plt.title("Frekuensi Peminjaman Sepeda Berdasarkan Kondisi Cuaca")
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Jumlah Peminjaman Sepeda")
    st.pyplot(fig)

elif visualization_choice == "Peminjaman per Hari":
    # Visualisasi peminjaman per hari
    fig = plt.figure(figsize=(10, 6))

    # Mengelompokkan data dan menghitung jumlah cnt pada hari dalam seminggu
    season_count = merged_df.groupby(by="weekday")["cnt"].sum().reset_index()

    # Membuat bar plot hari dalam seminggu
    sns.barplot(data=season_count, x="weekday", y="cnt", palette="viridis")
    plt.title("Frekuensi Peminjaman Sepeda Berdasarkan Hari dalam Seminggu")
    plt.xlabel("Weekday")
    plt.ylabel("Jumlah Peminjaman Sepeda")
    sns.barplot(x="weekday", y="cnt", data=merged_df.groupby("weekday")["cnt"].sum().reset_index())
    st.pyplot(fig)

elif visualization_choice == "Peminjaman per Hari Kerja":
    # Visualisasi peminjaman per hari kerja
    fig, ax = plt.subplots()
    # Menghitung jumlah peminjaman sepeda pada hari kerja
    workingday_counts = merged_df[merged_df['workingday'] == 'Yes']['cnt'].sum()
    non_workingday_counts = merged_df[merged_df['workingday'] == 'No']['cnt'].sum()

    # Menyiapkan data untuk pie chart
    labels_workingday = ['Working Day', 'Non-Working Day']
    sizes_workingday = [workingday_counts, non_workingday_counts]
    colors_workingday = ['#66b3ff', '#99ff99']

    # Membuat pie chart untuk workingday
    wedges, texts, autotexts = ax.pie(sizes_workingday, labels=labels_workingday,
                                      autopct=lambda p: '{:.0f} ({:.1f}%)'.format(p * sum(sizes_workingday) / 100, p),
                                      colors=colors_workingday, startangle=90, wedgeprops=dict(width=0.4))
    ax.axis('equal')  # Mengatur pie chart menjadi lingkaran

    # Menambahkan judul
    plt.title('Proporsi Peminjaman Sepeda di Hari Kerja')
    st.pyplot(fig)

elif visualization_choice == "Peminjaman per Hari Libur":
    # Visualisasi peminjaman per hari libur
    fig, ax = plt.subplots()
    # Menghitung jumlah peminjaman sepeda pada hari libur
    holiday_counts = merged_df[merged_df['holiday'] == 'Yes']['cnt'].sum()
    non_holiday_counts = merged_df[merged_df['holiday'] == 'No']['cnt'].sum()

    # Menyiapkan data untuk pie chart
    labels_holiday = ['Holiday', 'Non-Holiday']
    sizes_holiday = [holiday_counts, non_holiday_counts]
    colors_holiday = ['#66b3ff', '#99ff99']

    # Membuat pie chart untuk holiday
    wedges, texts, autotexts = ax.pie(sizes_holiday, labels=labels_holiday,
                                  autopct=lambda p: '{:.0f} ({:.1f}%)'.format(p * sum(sizes_holiday) / 100, p),
                                  colors=colors_holiday, startangle=90, wedgeprops=dict(width=0.4))
    ax.axis('equal')  # Mengatur pie chart menjadi lingkaran

    # Menambahkan judul
    plt.title('Proporsi Peminjaman Sepeda di Hari Libur')
    st.pyplot(fig)

elif visualization_choice == "Peminjaman per Rentang Jam":
    # Visualisasi peminjaman per hari libur
    fig = plt.figure(figsize=(10, 6))
    # Mengelompokkan data dan menghitung jumlah cnt pada setiap jam
    hr_count = merged_df.groupby(by="hr")["cnt"].sum().reset_index()

    # Membuat line plot untuk rentang jam
    sns.lineplot(data=hr_count, x="hr", y="cnt", marker="o", color="blue")
    plt.title("Frekuensi Peminjaman Sepeda Berdasarkan Jam")
    plt.xlabel("Jam (hr)")
    plt.ylabel("Jumlah Peminjaman Sepeda")
    plt.xticks(rotation=45)
    st.pyplot(fig)
