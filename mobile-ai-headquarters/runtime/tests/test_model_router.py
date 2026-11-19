import unittest
from model_router import ModelRouter, RouteBlocked

class RouterTests(unittest.TestCase):
    def config(self, providers):
        return {"budget_policy":{"mode":"zero_dollar","paid_calls_allowed":False},"providers":providers}
    def test_empty_pool_queues(self):
        with self.assertRaises(RouteBlocked): ModelRouter(self.config([]),{}).select({"capabilities":["reasoning"]})
    def test_paid_provider_never_selected(self):
        p={"id":"paid","enabled":True,"kind":"hosted","cost_class":"paid","verified_free":False,"quota_available":True,"data_terms_approved":True,"capabilities":["reasoning"],"endpoint":"https://invalid","model":"paid"}
        with self.assertRaises(RouteBlocked): ModelRouter(self.config([p]),{}).select({"capabilities":["reasoning"]})
    def test_verified_free_provider_selected(self):
        p={"id":"free","enabled":True,"kind":"hosted","cost_class":"free","verified_free":True,"quota_available":True,"data_terms_approved":True,"capabilities":["coding"],"endpoint":"https://invalid","model":"free","max_output_tokens":1000}
        route=ModelRouter(self.config([p]),{}).select({"capabilities":["coding"],"max_output_tokens":2000})
        self.assertEqual(route.provider_id,"free"); self.assertEqual(route.max_output_tokens,1000)
    def test_exhausted_quota_rejected(self):
        p={"id":"free","enabled":True,"kind":"hosted","cost_class":"free","verified_free":True,"quota_available":False,"data_terms_approved":True,"capabilities":["reasoning"],"endpoint":"https://invalid","model":"free"}
        with self.assertRaises(RouteBlocked): ModelRouter(self.config([p]),{}).select({"capabilities":["reasoning"]})
    def test_private_task_requires_local(self):
        hosted={"id":"hosted","enabled":True,"kind":"hosted","cost_class":"free","verified_free":True,"quota_available":True,"data_terms_approved":True,"capabilities":["summary"],"endpoint":"https://invalid","model":"hosted"}
        local={"id":"local","enabled":True,"kind":"local","cost_class":"free","verified_local":True,"capabilities":["summary"],"endpoint":"http://127.0.0.1:1234/v1/chat/completions","model":"local"}
        self.assertEqual(ModelRouter(self.config([hosted,local]),{}).select({"capabilities":["summary"],"privacy_sensitive":True}).provider_id,"local")

if __name__=="__main__": unittest.main()
