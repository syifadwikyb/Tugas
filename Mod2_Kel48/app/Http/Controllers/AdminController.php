<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Admin;
use Illuminate\Support\Facades\DB;

class AdminController extends Controller
{
    // Menampilkan halaman tambah admin
    public function create()
    {
        return view('admin.add');
    }

    // Menyimpan data admin baru
    public function store(Request $request)
    {
        $request->validate([
            'id_admin' => 'required',
            'nama_admin' => 'required',
            'alamat' => 'required',
            'username' => 'required',
            'password' => 'required',
        ]);

        Admin::create([
            'id_admin' => $request->id_admin,
            'nama_admin' => $request->nama_admin,
            'alamat' => $request->alamat,
            'username' => $request->username,
            'password' => bcrypt($request->password),
        ]);

        return redirect()->route('admin.index')->with('success', 'Data Admin berhasil disimpan');
    }

    // Menampilkan semua data admin yang aktif
    public function index()
    {
        $datas = Admin::whereNull('deleted_at')->get();
        return view('admin.index', compact('datas'));
    }

    // Menampilkan halaman edit admin
    public function edit($id)
    {
        $data = Admin::findOrFail($id);
        return view('admin.edit', compact('data'));
    }

    // Mengupdate data admin
    public function update(Request $request, $id)
    {
        $request->validate([
            'nama_admin' => 'required',
            'alamat' => 'required',
            'username' => 'required',
            'password' => 'required',
        ]);

        $admin = Admin::findOrFail($id);
        $admin->update([
            'nama_admin' => $request->nama_admin,
            'alamat' => $request->alamat,
            'username' => $request->username,
            'password' => bcrypt($request->password),
        ]);

        return redirect()->route('admin.index')->with('success', 'Data Admin berhasil diubah');
    }

    // Soft Delete - Memindahkan data ke Trash
    public function delete($id)
    {
        $admin = Admin::findOrFail($id);
        $admin->delete();

        return redirect()->route('admin.index')->with('success', 'Data Admin berhasil dipindahkan ke trash');
    }

    // Menampilkan halaman Trash (data yang dihapus)
    public function trash()
    {
        $datas = Admin::onlyTrashed()->get();
        return view('admin.trash', compact('datas'));
    }

    // Restore data dari Trash
    public function restore($id)
    {
        $admin = Admin::onlyTrashed()->where('id_admin', $id)->firstOrFail();
        $admin->restore();

        return redirect()->route('admin.trash')->with('success', 'Data Admin berhasil dikembalikan');
    }

    // Menghapus data secara permanen
    public function forceDelete($id)
    {
        $admin = Admin::onlyTrashed()->where('id_admin', $id)->firstOrFail();
        $admin->forceDelete();

        return redirect()->route('admin.trash')->with('success', 'Data Admin berhasil dihapus permanen');
    }

    public function exportCsv()
    {
        $admins = DB::table('admin')->get(); // Ambil semua data admin

        $filename = "admin_list_" . date('Y-m-d') . ".csv"; // Nama file CSV

        // Menulis data ke dalam format CSV
        $handle = fopen('php://output', 'w');
        fputcsv($handle, ['ID Admin', 'Nama', 'Alamat', 'Username']); // Header CSV

        foreach ($admins as $admin) {
            fputcsv($handle, [
                $admin->id_admin,
                $admin->nama_admin,
                $admin->alamat,
                $admin->username,
            ]);
        }

        fclose($handle);

        // Mengembalikan response sebagai file CSV
        return response()->streamDownload(function () use ($handle) {
            fclose($handle);
        }, $filename, [
            'Content-Type' => 'text/csv',
            'Cache-Control' => 'no-store, no-cache',
            'Pragma' => 'no-cache',
            'Expires' => '0',
        ]);
    }
}
