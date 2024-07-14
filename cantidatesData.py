import Cantidate
import OrganizedData

biden = Cantidate.cantidate(
    POSabortion = "legal under certain",
    POScrime = "placeholder",
    POSdefenseSpending = "less",
    POSeconemy ="placeholder",
    POSeducation = "more",
    POSguns = "more strict",
    POShealthcare = "public",
    POSimagration = "same",
    POSnationalSecurity ="placeholder",
    POStaxes = "same",
    DATAraw = OrganizedData.bidenRaw,
    DATArawList = OrganizedData.bidenRawList
)
# print(f"crime freq: {biden.cirmeFreq/len(biden.rawList)}")
# print(f"econemy freq: {biden.healthcareFreq/len(biden.rawList)}")
# print(f"national security freq: {biden.nationalSecurityFreq/len(biden.rawList)}")
# print(f"other freq: {biden.otherFreq/len(biden.rawList)}")

trump = Cantidate.cantidate(
    POSabortion = "illegal under all",
    POScrime = "placeholder",
    POSdefenseSpending = "more",
    POSeconemy ="placeholder",
    POSeducation = "less",
    POSguns = "less strict",
    POShealthcare = "placeholder",
    POSimagration = "decreased",
    POSnationalSecurity = "placeholder",
    POStaxes = "lower",
    DATAraw = OrganizedData.trumpRaw,
    DATArawList = OrganizedData.trumpRawList
)

obama = Cantidate.cantidate(
    POSabortion = "legal under certain",
    POScrime = "placeholder",
    POSdefenseSpending = "less",
    POSeconemy ="placeholder",
    POSeducation = "more",
    POSguns = "more strict",
    POShealthcare = "placeholder",
    #incresed deportations but incresed acces for differed action so evens out
    POSimagration = "same",
    POSnationalSecurity ="placeholder",
    POStaxes = "same",
    DATAraw = OrganizedData.obamaRaw,
    DATArawList = OrganizedData.obamaRawList
)

#not enough data + he's independant and recived 6.6% of the vote so it dose not matter
# anderson = Cantidate.cantidate(
#     POSabortion = "legal under certain",
#     POScrime = "placeholder",
#     POSdefenseSpending = "less",
#     POSeconemy ="placeholder",
#     POSeducation = "",
#     POSguns = "",
#     POShealthcare = "placeholder",
#     POSimagration = "",
#     POSnationalSecurity ="placeholder",
#     POStaxes = "",
#     DATAraw = OrganizedData.andersonRaw,
#     DATArawList = OrganizedData.andersonRawList
# )

reagen = Cantidate.cantidate(
    POSabortion = "illegal under all",
    POScrime = "placeholder",
    POSdefenseSpending = "increse",
    POSeconemy ="placeholder",
    POSeducation = "less",
    #he later in life changed his opinion
    POSguns = "less strict",
    POShealthcare = "placeholder",
    #did not support increse in border crossings but did call for all unocumented individuals in the us already to be given full citizenship
    POSimagration = "more",
    POSnationalSecurity ="placeholder",
    POStaxes = "lower",
    DATAraw = OrganizedData.reaganRaw,
    DATArawList = OrganizedData.reaganRawList
)

bush = Cantidate.cantidate(
    POSabortion = "illegal under all",
    POScrime = "placeholder",
    POSdefenseSpending = "increse",
    POSeconemy ="placeholder",
    POSeducation = "more",
    POSguns = "more strict",
    POShealthcare = "placeholder",
    POSimagration = "less",
    POSnationalSecurity ="placeholder",
    POStaxes = "lower",
    DATAraw = OrganizedData.bushRaw,
    DATArawList = OrganizedData.bushRawList
)

dukakis = Cantidate.cantidate(
    POSabortion = "legal under certain",
    POScrime = "placeholder",
    POSdefenseSpending = "decrease",
    POSeconemy ="placeholder",
    POSeducation = "more",
    POSguns = "more strict",
    POShealthcare = "placeholder",
    POSimagration = "same",
    POSnationalSecurity ="placeholder",
    POStaxes = "higher",
    DATAraw = OrganizedData.dukakisRaw,
    DATArawList = OrganizedData.dukakisRawList
)

kerry = Cantidate.cantidate(
    POSabortion = "legal under certain",
    POScrime = "placeholder",
    POSdefenseSpending = "less",
    POSeconemy ="placeholder",
    POSeducation = "more",
    POSguns = "more strict",
    POShealthcare = "placeholder",
    POSimagration = "same",
    POSnationalSecurity ="placeholder",
    POStaxes = "same",
    DATAraw = OrganizedData.kenedyRaw,
    DATArawList = OrganizedData.kenedyRawList
)

clinton = Cantidate.cantidate(
    POSabortion = "legal under certain",
    POScrime = "placeholder",
    POSdefenseSpending = "less",
    POSeconemy ="placeholder",
    POSeducation = "more",
    POSguns = "more strict",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.clintonRaw,
    DATArawList = OrganizedData.clintonRawList
)

Hclinton = Cantidate.cantidate(
    POSabortion = "",
    POScrime = "placeholder",
    POSdefenseSpending = "",
    POSeconemy ="placeholder",
    POSeducation = "",
    POSguns = "",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.HclintonRaw,
    DATArawList = OrganizedData.HclintonRawList
)

perot = Cantidate.cantidate(
    POSabortion = "",
    POScrime = "placeholder",
    POSdefenseSpending = "",
    POSeconemy ="placeholder",
    POSeducation = "",
    POSguns = "",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.perotRaw,
    DATArawList = OrganizedData.perotRawList
)

carter = Cantidate.cantidate(
    POSabortion = "",
    POScrime = "placeholder",
    POSdefenseSpending = "",
    POSeconemy ="placeholder",
    POSeducation = "",
    POSguns = "",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.carterRaw,
    DATArawList = OrganizedData.carterRawList
)

ford = Cantidate.cantidate(
    POSabortion = "",
    POScrime = "placeholder",
    POSdefenseSpending = "",
    POSeconemy ="placeholder",
    POSeducation = "",
    POSguns = "",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.fordRaw,
    DATArawList = OrganizedData.fordRawList
)

dole = Cantidate.cantidate(
    POSabortion = "",
    POScrime = "placeholder",
    POSdefenseSpending = "",
    POSeconemy ="placeholder",
    POSeducation = "",
    POSguns = "",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.doleRaw,
    DATArawList = OrganizedData.doleRawList
)

gore = Cantidate.cantidate(
    POSabortion = "",
    POScrime = "placeholder",
    POSdefenseSpending = "",
    POSeconemy ="placeholder",
    POSeducation = "",
    POSguns = "",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.goreRaw,
    DATArawList = OrganizedData.goreRawList
)

kenedy = Cantidate.cantidate(
    POSabortion = "",
    POScrime = "placeholder",
    POSdefenseSpending = "",
    POSeconemy ="placeholder",
    POSeducation = "",
    POSguns = "",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.kenedyRaw,
    DATArawList = OrganizedData.kenedyRawList
)

nixon = Cantidate.cantidate(
    POSabortion = "",
    POScrime = "placeholder",
    POSdefenseSpending = "",
    POSeconemy ="placeholder",
    POSeducation = "",
    POSguns = "",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.nixonRaw,
    DATArawList = OrganizedData.nixonRawList
)

mccain = Cantidate.cantidate(
    POSabortion = "",
    POScrime = "placeholder",
    POSdefenseSpending = "",
    POSeconemy ="placeholder",
    POSeducation = "",
    POSguns = "",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.mcainRaw,
    DATArawList = OrganizedData.mcainRawList
)

romney = Cantidate.cantidate(
    POSabortion = "",
    POScrime = "placeholder",
    POSdefenseSpending = "",
    POSeconemy ="placeholder",
    POSeducation = "",
    POSguns = "",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.romneyRaw,
    DATArawList = OrganizedData.romneyRawList
)

mondle = Cantidate.cantidate(
    POSabortion = "",
    POScrime = "placeholder",
    POSdefenseSpending = "",
    POSeconemy ="placeholder",
    POSeducation = "",
    POSguns = "",
    POShealthcare = "placeholder",
    POSimagration = "",
    POSnationalSecurity ="placeholder",
    POStaxes = "",
    DATAraw = OrganizedData.mondleRaw,
    DATArawList = OrganizedData.mondleRawList
)