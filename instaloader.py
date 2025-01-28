import instaloader

# Login ke Instagram
username = input("Masukkan username Instagram: ")
password = input("Masukkan password Instagram: ")

# Inisialisasi Instaloader
L = instaloader.Instaloader()

try:
    # Login ke akun pengguna
    L.login(username, password)
    print("Login berhasil!")
    
    # Dapatkan profil pengguna
    profile = instaloader.Profile.from_username(L.context, username)

    # Daftar akun yang di-follow dan yang mengikuti
    following = set(profile.get_followees())
    followers = set(profile.get_followers())

    # Cari akun yang tidak follow balik
    not_following_back = following - followers

    print("\nAkun yang tidak mem-follow balik:")
    for user in not_following_back:
        print(user.username)

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
