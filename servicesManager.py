import dbcontroller as db
import intent
import importlib as il
import threading

def startIntent(intent):
    skillName = intent.scriptName
    skillClass = il.import_module(f"skills.{skillName}")
    skillClass.Skill.init(intent)