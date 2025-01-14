from database import init_db, get_db
from models import add_student, get_students, update_student, delete_student

def main():
    init_db()  # Initialize database
    print("=== Aplikasi CRUD Mahasiswa ===")
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Lihat Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")

        choice = input("Pilih menu: ")
        if choice == "1":
            name = input("Nama: ")
            age = int(input("Umur: "))
            major = input("Jurusan: ")
            add_student(name, age, major)
        elif choice == "2":
            students = get_students()
            for student in students:
                print(student)
        elif choice == "3":
            student_id = int(input("ID Mahasiswa: "))
            name = input("Nama Baru: ")
            age = int(input("Umur Baru: "))
            major = input("Jurusan Baru: ")
            update_student(student_id, name, age, major)
        elif choice == "4":
            student_id = int(input("ID Mahasiswa: "))
            delete_student(student_id)
        elif choice == "5":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
