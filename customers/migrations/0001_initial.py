# Generated by Django 3.1.4 on 2021-01-03 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('first_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Last name')),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='Email address')),
                ('phone', models.CharField(blank=True, max_length=64, null=True, verbose_name='Phone number')),
                ('currency', models.CharField(blank=True, choices=[('AED', 'AED, Dirham'), ('AFN', 'AFN, Afghani'), ('ALL', 'ALL, Lek'), ('AMD', 'AMD, Dram'), ('ANG', 'ANG, Guilder'), ('AOA', 'AOA, Kwanza'), ('ARS', 'ARS, Peso'), ('AUD', 'AUD, Dollar'), ('AWG', 'AWG, Guilder'), ('AZN', 'AZN, Manat'), ('BAM', 'BAM, Marka'), ('BBD', 'BBD, Dollar'), ('BDT', 'BDT, Taka'), ('BGN', 'BGN, Lev'), ('BHD', 'BHD, Dinar'), ('BIF', 'BIF, Franc'), ('BMD', 'BMD, Dollar'), ('BND', 'BND, Dollar'), ('BOB', 'BOB, Boliviano'), ('BRL', 'BRL, Real'), ('BSD', 'BSD, Dollar'), ('BTN', 'BTN, Ngultrum'), ('BWP', 'BWP, Pula'), ('BYR', 'BYR, Ruble'), ('BZD', 'BZD, Dollar'), ('CAD', 'CAD, Dollar'), ('CDF', 'CDF, Franc'), ('CHF', 'CHF, Franc'), ('CLP', 'CLP, Peso'), ('CNY', 'CNY, Yuan Renminbi'), ('COP', 'COP, Peso'), ('CRC', 'CRC, Colon'), ('CUP', 'CUP, Peso'), ('CVE', 'CVE, Escudo'), ('CZK', 'CZK, Koruna'), ('DJF', 'DJF, Franc'), ('DKK', 'DKK, Krone'), ('DOP', 'DOP, Peso'), ('DZD', 'DZD, Dinar'), ('EGP', 'EGP, Pound'), ('ERN', 'ERN, Nakfa'), ('ETB', 'ETB, Birr'), ('EUR', 'EUR, Euro'), ('FJD', 'FJD, Dollar'), ('FKP', 'FKP, Pound'), ('GBP', 'GBP, Pound'), ('GEL', 'GEL, Lari'), ('GHS', 'GHS, Cedi'), ('GIP', 'GIP, Pound'), ('GMD', 'GMD, Dalasi'), ('GNF', 'GNF, Franc'), ('GTQ', 'GTQ, Quetzal'), ('GYD', 'GYD, Dollar'), ('HKD', 'HKD, Dollar'), ('HNL', 'HNL, Lempira'), ('HRK', 'HRK, Kuna'), ('HTG', 'HTG, Gourde'), ('HUF', 'HUF, Forint'), ('IDR', 'IDR, Rupiah'), ('ILS', 'ILS, Shekel'), ('INR', 'INR, Rupee'), ('IQD', 'IQD, Dinar'), ('IRR', 'IRR, Rial'), ('ISK', 'ISK, Krona'), ('JMD', 'JMD, Dollar'), ('JOD', 'JOD, Dinar'), ('JPY', 'JPY, Yen'), ('KES', 'KES, Shilling'), ('KGS', 'KGS, Som'), ('KHR', 'KHR, Riels'), ('KMF', 'KMF, Franc'), ('KPW', 'KPW, Won'), ('KRW', 'KRW, Won'), ('KWD', 'KWD, Dinar'), ('KYD', 'KYD, Dollar'), ('KZT', 'KZT, Tenge'), ('LAK', 'LAK, Kip'), ('LBP', 'LBP, Pound'), ('LKR', 'LKR, Rupee'), ('LRD', 'LRD, Dollar'), ('LSL', 'LSL, Loti'), ('LTL', 'LTL, Litas'), ('LVL', 'LVL, Lat'), ('LYD', 'LYD, Dinar'), ('MAD', 'MAD, Dirham'), ('MDL', 'MDL, Leu'), ('MGA', 'MGA, Ariary'), ('MKD', 'MKD, Denar'), ('MMK', 'MMK, Kyat'), ('MNT', 'MNT, Tugrik'), ('MOP', 'MOP, Pataca'), ('MRO', 'MRO, Ouguiya'), ('MUR', 'MUR, Rupee'), ('MVR', 'MVR, Rufiyaa'), ('MWK', 'MWK, Kwacha'), ('MXN', 'MXN, Peso'), ('MYR', 'MYR, Ringgit'), ('MZN', 'MZN, Metical'), ('NAD', 'NAD, Dollar'), ('NGN', 'NGN, Naira'), ('NIO', 'NIO, Cordoba'), ('NOK', 'NOK, Krone'), ('NPR', 'NPR, Rupee'), ('NZD', 'NZD, Dollar'), ('OMR', 'OMR, Rial'), ('PAB', 'PAB, Balboa'), ('PEN', 'PEN, Sol'), ('PGK', 'PGK, Kina'), ('PHP', 'PHP, Peso'), ('PKR', 'PKR, Rupee'), ('PLN', 'PLN, Zloty'), ('PYG', 'PYG, Guarani'), ('QAR', 'QAR, Rial'), ('RON', 'RON, Leu'), ('RSD', 'RSD, Dinar'), ('RUB', 'RUB, Ruble'), ('RWF', 'RWF, Franc'), ('SAR', 'SAR, Rial'), ('SBD', 'SBD, Dollar'), ('SCR', 'SCR, Rupee'), ('SDG', 'SDG, Pound'), ('SEK', 'SEK, Krona'), ('SGD', 'SGD, Dollar'), ('SHP', 'SHP, Pound'), ('SLL', 'SLL, Leone'), ('SOS', 'SOS, Shilling'), ('SRD', 'SRD, Dollar'), ('SSP', 'SSP, Pound'), ('STD', 'STD, Dobra'), ('SYP', 'SYP, Pound'), ('SZL', 'SZL, Lilangeni'), ('THB', 'THB, Baht'), ('TJS', 'TJS, Somoni'), ('TMT', 'TMT, Manat'), ('TND', 'TND, Dinar'), ('TOP', 'TOP, Paanga'), ('TRY', 'TRY, Lira'), ('TTD', 'TTD, Dollar'), ('TWD', 'TWD, Dollar'), ('TZS', 'TZS, Shilling'), ('UAH', 'UAH, Hryvnia'), ('UGX', 'UGX, Shilling'), ('USD', '$, Dollar'), ('UYU', 'UYU, Peso'), ('UZS', 'UZS, Som'), ('VEF', 'VEF, Bolivar'), ('VND', 'VND, Dong'), ('VUV', 'VUV, Vatu'), ('WST', 'WST, Tala'), ('XAF', 'XAF, Franc'), ('XCD', 'XCD, Dollar'), ('XOF', 'XOF, Franc'), ('XPF', 'XPF, Franc'), ('YER', 'YER, Rial'), ('ZAR', 'ZAR, Rand'), ('ZMK', 'ZMK, Kwacha'), ('ZWL', 'ZWL, Dollar')], max_length=3, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('synced_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=256, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=256, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=256, null=True, verbose_name='State')),
                ('zip_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Post/Zip-code')),
                ('country', models.CharField(blank=True, choices=[('GB', 'United Kingdom'), ('AF', 'Afghanistan'), ('AX', 'Aland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cape Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo, The Democratic Republic of the'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('CI', "Cote d'Ivoire"), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('VA', 'Holy See (Vatican City State)'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran, Islamic Republic of'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', "Korea, Democratic People's Republic of"), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libyan Arab Jamahiriya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia, The Former Yugoslav Republic of'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia, Federated States of'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('AN', 'Netherlands Antilles'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestinian Territory, Occupied'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Reunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('BL', 'Saint Barthelemy'), ('SH', 'Saint Helena'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia and the South Sandwich Islands'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard and Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan, Province of China'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania, United Republic of'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('US', 'United States'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela'), ('VN', 'Viet Nam'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=3, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
    ]