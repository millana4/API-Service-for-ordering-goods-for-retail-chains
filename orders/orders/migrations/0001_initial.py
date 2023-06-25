# Generated by Django 2.2.16 on 2023-06-25 10:59

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('provider', 'Поставщик'), ('buyer', 'Покупатель')], max_length=15, verbose_name='Роль пользователя')),
                ('first_name', models.CharField(max_length=15, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, max_length=15, null=True, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=15, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('company', models.CharField(max_length=30, verbose_name='Компания')),
                ('job_title', models.CharField(max_length=60, verbose_name='Должность')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('email',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('blanket', 'Корзина'), ('got', 'Принят'), ('confirmed', 'Подтвержден'), ('cancelled', 'Отменен'), ('assembling', 'Собирается'), ('delivering', 'Передан в доставку'), ('completed', 'Завершен')], max_length=15, verbose_name='Статус заказа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Характеристика')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Товар')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='orders.Category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('price_rrc', models.PositiveIntegerField(verbose_name='Рекомендуемая розничная цена')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_info', to='orders.Product', verbose_name='Товар')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Магазин')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ссылка на сайт')),
                ('reception_status', models.BooleanField(default=True, verbose_name='Прием заказов')),
                ('provider', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Поставщик')),
            ],
        ),
        migrations.CreateModel(
            name='ProductParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=40, verbose_name='Значение')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_parameter', to='orders.Product', verbose_name='Товар')),
                ('product_info', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_parameter', to='orders.ProductInfo', verbose_name='Информация о товаре')),
            ],
        ),
        migrations.AddField(
            model_name='productinfo',
            name='shop',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='priduct_info', to='orders.Shop', verbose_name='Магазин'),
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_info', to='orders.Order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_info', to='orders.Product', verbose_name='Товар')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_info', to='orders.Shop', verbose_name='Магазин')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Телефон')),
                ('city', models.CharField(max_length=15, verbose_name='Город')),
                ('street', models.CharField(max_length=20, verbose_name='Улица')),
                ('building', models.PositiveIntegerField(verbose_name='Номер дома')),
                ('additional_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Строение')),
                ('litera', models.CharField(blank=True, max_length=1, null=True, verbose_name='Литера')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='shop',
            field=models.ManyToManyField(related_name='categories', to='orders.Shop', verbose_name='Магазины'),
        ),
        migrations.AddConstraint(
            model_name='productinfo',
            constraint=models.UniqueConstraint(fields=('product', 'shop'), name=None),
        ),
        migrations.AddConstraint(
            model_name='orderinfo',
            constraint=models.UniqueConstraint(fields=('product', 'shop'), name=None),
        ),
    ]