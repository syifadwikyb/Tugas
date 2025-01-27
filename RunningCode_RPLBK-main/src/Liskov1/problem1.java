package Liskov1;

class Kendaraan {
    public void nyalakanMesin() {
        System.out.println("Mesin dinyalakan");
    }
}

class Mobil extends Kendaraan {
    // Mobil bisa menyalakan mesin
}

class Sepeda extends Kendaraan {
    @Override
    public void nyalakanMesin() {
        throw new UnsupportedOperationException("Sepeda tidak memiliki mesin");
    }
}

public class problem1 {
    public static void main(String[] args) {
        Kendaraan kendaraan1 = new Mobil();
        kendaraan1.nyalakanMesin(); // Berfungsi normal

        Kendaraan kendaraan2 = new Sepeda();
        kendaraan2.nyalakanMesin(); // Akan menimbulkan error UnsupportedOperationException
    }
}
