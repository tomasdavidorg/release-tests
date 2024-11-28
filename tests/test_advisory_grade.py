import datetime
import logging
import unittest
import dateutil
import dateutil.parser
import requests
import re

from oar.core.advisory import AdvisoryManager
from oar.core.advisory import Advisory
from oar.core.configstore import ConfigStore

from errata_tool import build

requests.packages.urllib3.util.connection.HAS_IPV6 = False
logging.basicConfig(level=logging.INFO)

class TestAdvisoryGrade(unittest.TestCase):


    def setUp(self):

        self.am = AdvisoryManager(ConfigStore("4.14.40"))
    
    def test(self):

    
        for ad in self.am.get_advisories():
            
            ad: Advisory = ad
            print(f"## Advisory: {ad.errata_id} Grade: {ad.get_overall_grade()}##")
            for n in ad.get_advisory_builds_nvrs():
                ad.get_advisory_build_grades(n)
            #ad.get_advisory_build_grades("node-feature-discovery-container-v4.14.0-202410182001.p0.g7e68ae8.assembly.stream.el8")
            #ad.get_advisory_build_grades("openshift-enterprise-hyperkube-container-v4.14.0-202410241808.p0.g03a907c.assembly.stream.el9")
        
        """
        
        nvrs = ad.get_advisory_builds_nvrs()
        print(f"## Advisory: {ad.errata_id} Grade: {ad.get_advisory_grade()} NVRs: {len(nvrs)} ##")
        for n in nvrs:
            ad.get_advisory_build_grades(n)
        """
        
        #print( datetime.datetime.strptime(ad.ship_date, "%Y-%b-%d"))


