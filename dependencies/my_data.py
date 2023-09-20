import requests


def get_thunder_data():
    try:
        smhi_data = requests.get("https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18/lat/59/data.json")
        smhi_data.raise_for_status()
        data_dict = smhi_data.json()
        tstm_dict = {}
        for timeseries in data_dict["timeSeries"]:
            time_data = timeseries["validTime"]
            for parameters in timeseries["parameters"]:
                if "tstm" in parameters["name"]:
                    tstm_dict[time_data[0:16].replace("T", " ")] = parameters["values"]

        return tstm_dict
    
    except:
        print("SMHI-DATA ERROR")
            
print(get_thunder_data())
