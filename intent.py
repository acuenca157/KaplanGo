class Intent:

    def __init__(self, scriptName, skillsPlaceholders, skillsUser) -> None:
        self.scriptName = scriptName
        if skillsUser != None:
            self.placeHolders = Intent.getPlaceHolders(skillsPlaceholders, skillsUser)
        else:
            self.placeHolders = None

    @staticmethod
    def getPlaceHolders(skillsPlaceholders, skillsUser):

        skillsPlaceholders = skillsPlaceholders.strip()
        skillsUser = skillsUser.strip()

        separators = ["{", "}"]

        for sep in separators:
            skillsPlaceholders = skillsPlaceholders.replace(sep, "")
        
        return {skillsPlaceholders : skillsUser}
