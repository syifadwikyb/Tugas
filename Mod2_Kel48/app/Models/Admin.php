<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes; // Tambahkan ini

class Admin extends Model
{
    use HasFactory, SoftDeletes; // Tambahkan SoftDeletes

    protected $table = 'admin';
    protected $primaryKey = 'id_admin';
    protected $fillable = ['id_admin', 'nama_admin', 'alamat', 'username', 'password'];

    protected $dates = ['deleted_at']; // Pastikan kolom deleted_at dikenali
}
