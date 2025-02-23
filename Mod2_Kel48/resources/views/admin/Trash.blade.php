@extends('admin.layout')

@section('content')
<h4 class="mt-5">Trash Data Admin</h4>

<a href="{{ route('admin.index') }}" class="btn btn-primary">Kembali ke Data Admin</a>

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
                <td>
                    <form method="POST" action="{{ route('admin.restore', $data->id_admin) }}">
                        @csrf
                        <button type="submit" class="btn btn-success">Restore</button>
                    </form>

                    <form method="POST" action="{{ route('admin.forceDelete', $data->id_admin) }}" class="d-inline">
                        @csrf
                        <button type="submit" class="btn btn-danger" onclick="return confirm('Yakin hapus permanen?')">Hapus Permanen</button>
                    </form>
                </td>
            </tr>
        @endforeach
    </tbody>
</table>
@stop
