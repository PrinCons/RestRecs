import kagglehub

# Download latest version
datasets = [
    "rayhan32/trip-advisor-newyork-city-restaurants-dataset-10k",
    "beridzeg45/nyc-restaurants",
    "anoopjohny/new-york-restaurant-menus-and-details",
    "new-york-city/nyc-inspections"
    ]
for dataset in datasets:
    path = kagglehub.dataset_download(dataset)
    print("find ", dataset.split("/")[-1].replace("-", " "))
    print("--HERE--")
    print(path)