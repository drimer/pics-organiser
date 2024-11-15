import click


@click.group()
def cli():
    pass


from tasks.reports import report_imgs_without_exif_date

    
@cli.command()
@click.option('--dir-path', help='Path to the folder with the images')
def report(dir_path):
    report_imgs_without_exif_date(dir_path)
    