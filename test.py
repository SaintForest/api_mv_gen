import pytest
import inference

def test_argument_length(capsys):
    '''This test checks the argument vector has only one arguments. Title and description'''
    inference.main(['--description','The evil iago pretends to be friend of Othello in order to manipulate him to serve his own end in the film version of the Shakespeare classic'])
    out, err = capsys.readouterr()
    assert 'Correct number of arguments\n' in out

def test_arguments_present(capsys):
    '''This test checks whether the arguments in the argument vector are named title and description.'''
    inference.main(['--description','The evil iago pretends to be friend of Othello in order to manipulate him to serve his own end in the film version of the Shakespeare classic'])
    out, err = capsys.readouterr()
    assert 'description is present\n' in out

def test_description_length(capsys):
    '''This test checks whether the parameter in the description argument has correct length of characters and words.'''
    inference.main(['--description','The evil iago pretends to be friend of Othello in order to manipulate him to serve his own end in the film version of the Shakespeare classic'])
    out, err = capsys.readouterr()
    assert 'Description argument has words and characters in range\n' in out

def test_specialchars_inputs(capsys):
    '''This test checks whether the parameter values for description have only alphanumeric characters.'''
    inference.main(['--description','The evil iago pretends to be friend of Othello in order to manipulate him to serve his own end in the film version of the Shakespeare classic'])
    out, err = capsys.readouterr()
    assert 'description have only alphanumeric characters\n' in out