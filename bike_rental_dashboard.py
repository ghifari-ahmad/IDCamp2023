import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca data day.csv dan hour.csv
day_df = pd.read_csv('/gdrive/MyDrive/Kaggle/day.csv')
hour_df = pd.read_csv('/gdrive/MyDrive/Kaggle/hour.csv')

# Mengubah tipe data pada kolom "dteday" menjadi datetime
datetime_columns = ["dteday"]

for column in datetime_columns:
  day_df[column] = pd.to_datetime(day_df[column])

# Mengganti nilai 0 dengan 2011 dan nilai 1 dengan 2012 pada kolom 'yr'
day_df['yr'] = day_df['yr'].replace({0: 2011, 1: 2012})

# Mengubah keterangan nilai untuk variabel 'season' dengan dictionary
season_mapping = {
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
    4: 'Winter'
}

# Mengganti nilai pada kolom 'season' menggunakan dictionary penggantian
day_df['season'] = day_df['season'].replace(season_mapping)

# Mengganti nilai 0 dengan 'No' dan nilai 1 dengan 'Yes' pada kolom 'holiday'
day_df['holiday'] = day_df['holiday'].replace({0: 'No', 1: 'Yes'})

# Mengubah keterangan nilai untuk variabel 'weekday' dengan dictionary
weekday_mapping = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

# Mengganti nilai pada kolom 'weekday' menggunakan dictionary penggantian
day_df['weekday'] = day_df['weekday'].replace(weekday_mapping)

# Mengganti nilai 0 dengan 'No' dan nilai 1 dengan 'Yes' pada kolom 'workingday'
day_df['workingday'] = day_df['workingday'].replace({0: 'No', 1: 'Yes'})

# Mengubah keterangan nilai untuk variabel 'weathersit' dengan dictionary
weathersit_mapping = {
    1: 'Clear',
    2: 'Mist',
    3: 'Light Rain',
    4: 'Heavy Rain'
}

# Mengganti nilai pada kolom 'weathersit' menggunakan dictionary penggantian
day_df['weathersit'] = day_df['weathersit'].replace(weathersit_mapping)

# Mengubah nilai kolom 'temp', 'atemp', 'hum', 'windspeed' menggunakan skala sebenarnya
max_temp = 41
max_atemp = 50
max_hum = 100
max_windspeed = 67

day_df['temp'] = day_df['temp'] * max_temp
day_df['atemp'] = day_df['atemp'] * max_atemp
day_df['hum'] = day_df['hum'] * max_hum
day_df['windspeed'] = day_df['windspeed'] * max_windspeed

# Mengubah tipe data pada kolom "dteday" menjadi datetime
datetime_columns = ["dteday"]

for column in datetime_columns:
  hour_df[column] = pd.to_datetime(hour_df[column])

# Memeriksa tipe data tiap kolom
hour_df.info()

# Mengganti nilai 0 dengan 2011 dan nilai 1 dengan 2012 pada kolom 'yr'
hour_df['yr'] = hour_df['yr'].replace({0: 2011, 1: 2012})

# Mengubah keterangan nilai untuk variabel 'season' dengan dictionary
season_mapping = {
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
    4: 'Winter'
}

# Mengganti nilai pada kolom 'season' menggunakan dictionary penggantian
hour_df['season'] = hour_df['season'].replace(season_mapping)

# Mengubah keterangan nilai untuk variabel 'hr' dengan dictionary
hr_mapping = {
    0: '00:00 - 04:00', 1: '00:00 - 04:00', 2: '00:00 - 04:00', 3: '00:00 - 04:00',
    4: '04:00 - 08:00', 5: '04:00 - 08:00', 6: '04:00 - 08:00', 7: '04:00 - 08:00',
    8: '08:00 - 12:00', 9: '08:00 - 12:00', 10: '08:00 - 12:00', 11: '08:00 - 12:00',
    12: '12:00 - 16:00', 13: '12:00 - 16:00', 14: '12:00 - 16:00', 15: '12:00 - 16:00',
    16: '16:00 - 20:00', 17: '16:00 - 20:00', 18: '16:00 - 20:00', 19: '16:00 - 20:00',
    20: '20:00 - 00:00', 21: '20:00 - 00:00', 22: '20:00 - 00:00', 23: '20:00 - 00:00'
}

# Mengganti nilai pada kolom 'season' menggunakan dictionary penggantian
hour_df['hr'] = hour_df['hr'].replace(hr_mapping)

# Mengubah keterangan nilai untuk variabel 'weekday' dengan dictionary
weekday_mapping = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

# Mengganti nilai pada kolom 'weekday' menggunakan dictionary penggantian
hour_df['weekday'] = hour_df['weekday'].replace(weekday_mapping)

# Mengganti nilai 0 dengan 'No' dan nilai 1 dengan 'Yes' pada kolom 'workingday'
hour_df['workingday'] = hour_df['workingday'].replace({0: 'No', 1: 'Yes'})

# Mengganti nilai 0 dengan 'No' dan nilai 1 dengan 'Yes' pada kolom 'holiday'
hour_df['holiday'] = hour_df['holiday'].replace({0: 'No', 1: 'Yes'})

# Mengubah keterangan nilai untuk variabel 'weathersit' dengan dictionary
weathersit_mapping = {
    1: 'Clear',
    2: 'Mist',
    3: 'Light Rain',
    4: 'Heavy Rain'
}

# Mengganti nilai pada kolom 'weathersit' menggunakan kamus penggantian
hour_df['weathersit'] = hour_df['weathersit'].replace(weathersit_mapping)

# Mengubah nilai kolom 'temp', 'atemp', 'hum', 'windspeed' menggunakan skala sebenarnya
max_temp = 41
max_atemp = 50
max_hum = 100
max_windspeed = 67

hour_df['temp'] = hour_df['temp'] * max_temp
hour_df['atemp'] = hour_df['atemp'] * max_atemp
hour_df['hum'] = hour_df['hum'] * max_hum
hour_df['windspeed'] = hour_df['windspeed'] * max_windspeed

# Melakukan merge antara day_df dan hour_df berdasarkan kolom 'count'
merged_df = pd.merge(day_df, hour_df, how='left', left_on='instant', right_on='instant', suffixes=('_day', '_hour'))

# Menggabungkan kolom dengan sufiks _x dan _y
for col in merged_df.columns:
    if col.endswith('_day'):
        merged_df[col[:-4]] = merged_df[col].combine_first(merged_df[col[:-4] + '_hour'])

# Menghapus kolom yang memiliki sufiks _x dan _y
merged_df = merged_df.drop(columns=[col for col in merged_df.columns if col.endswith(('_day', '_hour'))])

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