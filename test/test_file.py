import os

from files.file import File


def test_that_parent_folders_include_all():
    file = File(os.path.join('root', '2010', '09', '15', '00001.jpg'))

    assert file.parent_folders_as_list == ['root', '2010', '09', '15']


def test_that_parent_folders_can_be_empty():
    file = File(os.path.join('00001.jpg'))

    assert file.parent_folders_as_list == []
