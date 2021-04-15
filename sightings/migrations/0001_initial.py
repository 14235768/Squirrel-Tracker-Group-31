# Generated by Django 3.1.2 on 2021-04-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('latitude', models.DecimalField(decimal_places=15, default=0, help_text='Latitude of the squirrel', max_digits=17)),
                ('longitude', models.DecimalField(decimal_places=14, help_text='Longitude of the squirrel', max_digits=16)),
                ('unique_squirrel_id', models.CharField(help_text='unique ID of the squirrel', max_length=14, primary_key=True, serialize=False)),
                ('hectare', models.CharField(blank=True, default='', help_text='combination of one axis that runs N-S (01~42) + another axis that runs E-W (A-I)', max_length=3)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='PM', help_text='AM or PM', max_length=10)),
                ('date', models.DateField(blank=True, default=None, help_text='Date when you saw the squirrel', null=True)),
                ('hectare_squirrel_number', models.IntegerField(blank=True, default='1')),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('unknown', 'unknown')], default='Adult', help_text='your guess: how old was the squirrel?', max_length=20)),
                ('primary_fur_color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='primary fur color of the squirrel seen', max_length=15)),
                ('highlight_fur_color', models.CharField(blank=True, default='', max_length=20)),
                ('color_notes', models.CharField(blank=True, default='', max_length=160)),
                ('location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], max_length=15)),
                ('specific_location', models.CharField(blank=True, default='', max_length=120)),
                ('running', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Was the squirrel running?', max_length=10)),
                ('chasing', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Was the squirrel chasing something?', max_length=10)),
                ('climbing', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Was the squirrel climbing?', max_length=10)),
                ('eating', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Was the squirrel eating?', max_length=10)),
                ('foraging', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Was the squirrel foraging?', max_length=10)),
                ('other_activities', models.CharField(blank=True, default='', max_length=160)),
                ('kuks', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Squirrel was heard kukking, a chirpy vocal communication used for a variety of reasons.', max_length=10)),
                ('quaas', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog.', max_length=10)),
                ('moans', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk.', max_length=10)),
                ('tail_flags', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text="Squirrel was seen flagging its tail. Flagging is a whipping motion used to exaggerate squirrel's size and confuse rivals or predators. Looks as if the squirrel is scribbling with tail into the air.", max_length=10)),
                ('tail_twitch', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Squirrel was seen twitching its tail. Looks like a wave running through the tail, like a breakdancer doing the arm wave. Often used to communicate interest, curiosity.', max_length=10)),
                ('approaches', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Squirrel was seen approaching human, seeking food.', max_length=10)),
                ('indifferent', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Squirrel was indifferent to human presence.', max_length=10)),
                ('runs_from', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Squirrel was seen running from humans, seeing them as a threat.', max_length=10)),
                ('other_interactions', models.CharField(blank=True, default='', max_length=120)),
            ],
        ),
    ]
