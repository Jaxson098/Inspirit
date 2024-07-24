import Cantidate
import OrganizedData

biden = Cantidate.cantidate(
    DATAraw = OrganizedData.bidenRaw,
    DATArawList = OrganizedData.bidenRawList
)
# print(f"crime freq: {biden.cirmeFreq/len(biden.rawList)}")
# print(f"econemy freq: {biden.healthcareFreq/len(biden.rawList)}")
# print(f"national security freq: {biden.nationalSecurityFreq/len(biden.rawList)}")
# print(f"other freq: {biden.otherFreq/len(biden.rawList)}")

trump = Cantidate.cantidate(
    DATAraw = OrganizedData.trumpRaw,
    DATArawList = OrganizedData.trumpRawList
)

obama = Cantidate.cantidate(
    DATAraw = OrganizedData.obamaRaw,
    DATArawList = OrganizedData.obamaRawList
)

reagen = Cantidate.cantidate(
    DATAraw = OrganizedData.reaganRaw,
    DATArawList = OrganizedData.reaganRawList
)

bush = Cantidate.cantidate(
    DATAraw = OrganizedData.bushRaw,
    DATArawList = OrganizedData.bushRawList
)

dukakis = Cantidate.cantidate(
    DATAraw = OrganizedData.dukakisRaw,
    DATArawList = OrganizedData.dukakisRawList
)

kerry = Cantidate.cantidate(
    DATAraw = OrganizedData.kenedyRaw,
    DATArawList = OrganizedData.kenedyRawList
)

clinton = Cantidate.cantidate(
    DATAraw = OrganizedData.clintonRaw,
    DATArawList = OrganizedData.clintonRawList
)

Hclinton = Cantidate.cantidate(
    DATAraw = OrganizedData.HclintonRaw,
    DATArawList = OrganizedData.HclintonRawList
)

perot = Cantidate.cantidate(
    DATAraw = OrganizedData.perotRaw,
    DATArawList = OrganizedData.perotRawList
)

carter = Cantidate.cantidate(
    DATAraw = OrganizedData.carterRaw,
    DATArawList = OrganizedData.carterRawList
)

ford = Cantidate.cantidate(
    DATAraw = OrganizedData.fordRaw,
    DATArawList = OrganizedData.fordRawList
)

dole = Cantidate.cantidate(
    DATAraw = OrganizedData.doleRaw,
    DATArawList = OrganizedData.doleRawList
)

gore = Cantidate.cantidate(
    DATAraw = OrganizedData.goreRaw,
    DATArawList = OrganizedData.goreRawList
)

kenedy = Cantidate.cantidate(
    DATAraw = OrganizedData.kenedyRaw,
    DATArawList = OrganizedData.kenedyRawList
)

nixon = Cantidate.cantidate(
    DATAraw = OrganizedData.nixonRaw,
    DATArawList = OrganizedData.nixonRawList
)

mccain = Cantidate.cantidate(
    DATAraw = OrganizedData.mcainRaw,
    DATArawList = OrganizedData.mcainRawList
)

romney = Cantidate.cantidate(
    DATAraw = OrganizedData.romneyRaw,
    DATArawList = OrganizedData.romneyRawList
)

mondle = Cantidate.cantidate(
    DATAraw = OrganizedData.mondleRaw,
    DATArawList = OrganizedData.mondleRawList
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