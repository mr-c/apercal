import unittest
import matplotlib as mpl
mpl.use('TkAgg')
from apercal.modules.prepare import prepare

from os import path

here = path.dirname(__file__)


class TestPrepare(unittest.TestCase):

    def test_prepare(self):
        p = prepare(path.join(here, 'test.cfg'))
        p.apercaldir = path.join(here, '../')
        p.basedir = path.join(here, '../data/small/')
        p.fluxcal = '3C295.MS'
        p.polcal = '3C138.MS'
        p.target = 'NGC807.MS'
        #p.show(showall=False)
        p.go()

