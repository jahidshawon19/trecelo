from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0003_product_back_part_image_product_challenge_part_image_and_more'),
    ]

    operations = [
        migrations.RenameModel('Product', 'Sample'),
    ]
