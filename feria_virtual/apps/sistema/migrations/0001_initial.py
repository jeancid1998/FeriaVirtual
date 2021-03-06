# Generated by Django 3.1.1 on 2020-09-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatPersonal',
            fields=[
                ('id_dat', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_nom', models.CharField(max_length=15)),
                ('ape_mat', models.CharField(max_length=15)),
                ('ape_pat', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'dat_personal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetallCompra',
            fields=[
                ('id_detall', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_detall', models.DateField()),
                ('nom_producto', models.CharField(max_length=15)),
                ('cost_producto', models.IntegerField()),
                ('iva_producto', models.IntegerField()),
                ('total_compra', models.IntegerField()),
            ],
            options={
                'db_table': 'detall_compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DirecExtran',
            fields=[
                ('id_direc', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pais', models.CharField(max_length=20)),
                ('direc_cli', models.CharField(max_length=20)),
                ('num_calle', models.IntegerField(blank=True, null=True)),
                ('depto', models.CharField(blank=True, max_length=10, null=True)),
                ('localidad', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'direc_extran',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DirecLocal',
            fields=[
                ('id_direc', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('direc_cli', models.CharField(max_length=20)),
                ('num_calle', models.IntegerField(blank=True, null=True)),
                ('depto', models.CharField(blank=True, max_length=10, null=True)),
                ('region', models.CharField(max_length=20)),
                ('comuna', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'direc_local',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProcesVenta',
            fields=[
                ('id_venta', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'proces_venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_prod', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prod', models.CharField(max_length=20)),
                ('precio_prod', models.IntegerField()),
                ('stock_prod', models.IntegerField()),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('email', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('confir_contra', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'registro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id_report', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_report', models.DateField()),
                ('tip_report', models.CharField(max_length=15)),
                ('user_report', models.CharField(max_length=15)),
                ('descrip_report', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'reportes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReportMerma',
            fields=[
                ('id_merma', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_merma', models.DateField()),
                ('descrip_merma', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'report_merma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReportVenta',
            fields=[
                ('id_report_vent', models.IntegerField(primary_key=True, serialize=False)),
                ('prod_venta', models.CharField(max_length=20)),
                ('cant_venta', models.IntegerField()),
                ('total_venta', models.IntegerField()),
            ],
            options={
                'db_table': 'report_venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('est_seguimiento', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'seguimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeguiProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('est_segui', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'segui_prod',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subastas',
            fields=[
                ('id_sub', models.IntegerField(primary_key=True, serialize=False)),
                ('min_postor', models.IntegerField()),
            ],
            options={
                'db_table': 'subastas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubaTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'suba_trans',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id_trans', models.IntegerField(primary_key=True, serialize=False)),
                ('tip_transporte', models.CharField(max_length=15)),
                ('tamano_trans', models.IntegerField()),
                ('capacidad_trans', models.IntegerField()),
                ('refrigeracion_trans', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'transporte',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'user_report',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuariosUsuarios',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField()),
                ('is_staff', models.BooleanField()),
                ('tipo_usuario', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'usuarios_usuarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VentExtran',
            fields=[
                ('id_vent_ex', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom_cli', models.CharField(max_length=20)),
                ('ape_pat', models.CharField(max_length=20)),
                ('ape_mat', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'vent_extran',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VentLocal',
            fields=[
                ('id_vent_loc', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom_cli', models.CharField(max_length=20)),
                ('ape_pat', models.CharField(max_length=20)),
                ('ape_mat', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'vent_local',
                'managed': False,
            },
        ),
    ]
