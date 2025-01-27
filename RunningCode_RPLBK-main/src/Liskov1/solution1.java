//package Liskov1;

class Kendaraan {
    // Kelas umum untuk kendaraan
}

class KendaraanBermesin extends Kendaraan {
    public void nyalakanMesin() {
        System.out.println("Mesin dinyalakan");
    }
}

class Mobil extends KendaraanBermesin {
    // Mobil bisa menyalakan mesin
}

class Sepeda extends Kendaraan {
    // Sepeda tidak memiliki mesin, jadi tidak memerlukan metode nyalakanMesin
}

public class solution1 {
    public static void main(String[] args) {
        KendaraanBermesin kendaraan1 = new Mobil();
        kendaraan1.nyalakanMesin(); // Berfungsi normal untuk kendaraan bermesin

        Kendaraan kendaraan2 = new Sepeda();
        // Sepeda tidak memiliki metode nyalakanMesin, jadi tidak ada error
    }
}
