@extends('admin.layout')

@section('content')
    <h4 class="mt-5">Trash Data Admin</h4>

    <div class="d-flex gap-2 align-items-center mb-3">
        <a href="{{ route('admin.index') }}" class="btn btn-primary">Kembali ke Data Admin</a>

        <!-- Tombol untuk mengembalikan semua data -->
        <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#restoreAllModal">
            Kembalikan Semua Data
        </button>

        <!-- Tombol untuk menghapus permanen semua data -->
        <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#deleteAllModal">
            Hapus Permanen Semua
        </button>
    </div>

    @if ($message = Session::get('success'))
        <div class="alert alert-success mt-3">{{ $message }}</div>
    @endif

    <table class="table table-hover mt-2">
        <thead>
            <tr>
                <th>No.</th>
                <th>Nama</th>
                <th>Alamat</th>
                <th>Username</th>
                <th>Action</th>
            </tr>
        </thead>

        <tbody>
            @foreach ($datas as $data)
                <tr>
                    <td>{{ $data->id_admin }}</td>
                    <td>{{ $data->nama_admin }}</td>
                    <td>{{ $data->alamat }}</td>
                    <td>{{ $data->username }}</td>
                    <td class="d-flex gap-2">
                        <!-- Tombol Kembalikan -->
                        <button type="button" class="btn btn-success" data-bs-toggle="modal"
                            data-bs-target="#restoreModal{{ $data->id_admin }}">
                            Kembalikan
                        </button>

                        <!-- Tombol Hapus Permanen -->
                        <button type="button" class="btn btn-danger" data-bs-toggle="modal"
                            data-bs-target="#deleteModal{{ $data->id_admin }}">
                            Hapus Permanen
                        </button>
                    </td>
                </tr>

                <!-- Modal Konfirmasi "Kembalikan Data" -->
                <div class="modal fade" id="restoreModal{{ $data->id_admin }}" tabindex="-1"
                    aria-labelledby="restoreModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">Konfirmasi Pengembalian</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal"
                                    aria-label="Close"></button>
                            </div>
                            <form method="POST" action="{{ route('admin.restore', $data->id_admin) }}">
                                @csrf
                                <div class="modal-body">
                                    Apakah Anda ingin mengembalikan data ini?
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Tutup</button>
                                    <button type="submit" class="btn btn-primary">Ya</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>

                <!-- Modal Konfirmasi "Hapus Permanen Data" -->
                <div class="modal fade" id="deleteModal{{ $data->id_admin }}" tabindex="-1"
                    aria-labelledby="deleteModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">Konfirmasi Hapus Permanen</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal"
                                    aria-label="Close"></button>
                            </div>
                            <form method="POST" action="{{ route('admin.forceDelete', $data->id_admin) }}">
                                @csrf
                                <div class="modal-body">
                                    Apakah Anda yakin ingin menghapus data ini secara permanen?
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Tutup</button>
                                    <button type="submit" class="btn btn-danger">Ya</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            @endforeach
        </tbody>
    </table>

    <div class="modal fade" id="restoreAllModal" tabindex="-1" aria-labelledby="restoreAllModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Konfirmasi Pengembalian Semua Data</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form method="POST" action="{{ route('admin.restore.all') }}">
                    @csrf
                    <div class="modal-body">
                        Apakah Anda ingin mengembalikan semua data yang telah dihapus?
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Tutup</button>
                        <button type="submit" class="btn btn-primary">Ya</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <div class="modal fade" id="deleteAllModal" tabindex="-1" aria-labelledby="deleteAllModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Konfirmasi Hapus Permanen Semua Data</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form method="POST" action="{{ route('admin.forceDelete.all') }}">
                    @csrf
                    <div class="modal-body">
                        Apakah Anda yakin ingin menghapus semua data secara permanen?
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Tutup</button>
                        <button type="submit" class="btn btn-danger">Ya</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

@stop
