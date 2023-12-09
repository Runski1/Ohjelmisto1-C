'use strict';
const cityData = [
  {
    "id": "1",
    "name": "Tirana",
    "country": "Albania",
    "latitude_deg": "41.4147",
    "longitude_deg": "19.7206",
    "port_city": "0"
  },
  {
    "id": "2",
    "name": "Vienna",
    "country": "Austria",
    "latitude_deg": "48.1103",
    "longitude_deg": "16.5697",
    "port_city": "0"
  },
  {
    "id": "3",
    "name": "Sarajevo",
    "country": "Bosnia and Herzegovina",
    "latitude_deg": "43.8246",
    "longitude_deg": "18.3315",
    "port_city": "0"
  },
  {
    "id": "4",
    "name": "Brussels",
    "country": "Belgium",
    "latitude_deg": "50.9014",
    "longitude_deg": "4.48444",
    "port_city": "0"
  },
  {
    "id": "5",
    "name": "Sofia",
    "country": "Bulgaria",
    "latitude_deg": "42.6967",
    "longitude_deg": "23.4114",
    "port_city": "0"
  },
  {
    "id": "6",
    "name": "Minsk",
    "country": "Belarus",
    "latitude_deg": "53.8881",
    "longitude_deg": "28.04",
    "port_city": "0"
  },
  {
    "id": "7",
    "name": "Zurich",
    "country": "Switzerland",
    "latitude_deg": "47.4581",
    "longitude_deg": "8.54806",
    "port_city": "0"
  },
  {
    "id": "8",
    "name": "Prague",
    "country": "Czech Republic",
    "latitude_deg": "50.1008",
    "longitude_deg": "14.26",
    "port_city": "0"
  },
  {
    "id": "9",
    "name": "Berlin",
    "country": "Germany",
    "latitude_deg": "52.3514",
    "longitude_deg": "13.4939",
    "port_city": "0"
  },
  {
    "id": "10",
    "name": "Copenhagen",
    "country": "Denmark",
    "latitude_deg": "55.6179",
    "longitude_deg": "12.656",
    "port_city": "1"
  },
  {
    "id": "11",
    "name": "Algiers",
    "country": "Algeria",
    "latitude_deg": "36.691",
    "longitude_deg": "3.21541",
    "port_city": "1"
  },
  {
    "id": "12",
    "name": "Tallinn",
    "country": "Estonia",
    "latitude_deg": "59.4133",
    "longitude_deg": "24.8328",
    "port_city": "1"
  },
  {
    "id": "13",
    "name": "Cairo",
    "country": "Egypt",
    "latitude_deg": "30.1219",
    "longitude_deg": "31.4056",
    "port_city": "1"
  },
  {
    "id": "14",
    "name": "Gran-Canaria",
    "country": "Canary islands",
    "latitude_deg": "27.9319",
    "longitude_deg": "-15.3866",
    "port_city": "1"
  },
  {
    "id": "15",
    "name": "Madrid",
    "country": "Spain",
    "latitude_deg": "40.4719",
    "longitude_deg": "-3.56264",
    "port_city": "0"
  },
  {
    "id": "16",
    "name": "Helsinki",
    "country": "Finland",
    "latitude_deg": "60.3172",
    "longitude_deg": "24.9633",
    "port_city": "1"
  },
  {
    "id": "17",
    "name": "Paris",
    "country": "France",
    "latitude_deg": "49.0128",
    "longitude_deg": "2.55",
    "port_city": "0"
  },
  {
    "id": "18",
    "name": "London",
    "country": "United Kingdom",
    "latitude_deg": "51.4706",
    "longitude_deg": "-0.461941",
    "port_city": "1"
  },
  {
    "id": "19",
    "name": "Mestia",
    "country": "Georgia",
    "latitude_deg": "43.0536",
    "longitude_deg": "42.749",
    "port_city": "0"
  },
  {
    "id": "20",
    "name": "Athens",
    "country": "Greece",
    "latitude_deg": "37.9364",
    "longitude_deg": "23.9445",
    "port_city": "1"
  },
  {
    "id": "21",
    "name": "Zagreb",
    "country": "Croatia",
    "latitude_deg": "45.7429",
    "longitude_deg": "16.0688",
    "port_city": "0"
  },
  {
    "id": "22",
    "name": "Budapest",
    "country": "Hungary",
    "latitude_deg": "47.4298",
    "longitude_deg": "19.2611",
    "port_city": "0"
  },
  {
    "id": "23",
    "name": "Dublin",
    "country": "Ireland",
    "latitude_deg": "53.4213",
    "longitude_deg": "-6.27007",
    "port_city": "1"
  },
  {
    "id": "24",
    "name": "Reykjavik",
    "country": "Iceland",
    "latitude_deg": "63.985",
    "longitude_deg": "-22.6056",
    "port_city": "1"
  },
  {
    "id": "25",
    "name": "Rome",
    "country": "Italy",
    "latitude_deg": "41.8045",
    "longitude_deg": "12.252",
    "port_city": "1"
  },
  {
    "id": "26",
    "name": "Vilnius",
    "country": "Lithuania",
    "latitude_deg": "54.6341",
    "longitude_deg": "25.2858",
    "port_city": "0"
  },
  {
    "id": "27",
    "name": "Luxembourg",
    "country": "Luxembourg",
    "latitude_deg": "49.6233",
    "longitude_deg": "6.20444",
    "port_city": "0"
  },
  {
    "id": "28",
    "name": "Riga",
    "country": "Latvia",
    "latitude_deg": "56.9236",
    "longitude_deg": "23.9711",
    "port_city": "1"
  },
  {
    "id": "29",
    "name": "Tripoli",
    "country": "Libya",
    "latitude_deg": "32.6635",
    "longitude_deg": "13.159",
    "port_city": "1"
  },
  {
    "id": "30",
    "name": "Casablanca",
    "country": "Morocco",
    "latitude_deg": "33.3675",
    "longitude_deg": "-7.58997",
    "port_city": "1"
  },
  {
    "id": "31",
    "name": "Chisinau",
    "country": "Moldova",
    "latitude_deg": "46.9277",
    "longitude_deg": "28.931",
    "port_city": "0"
  },
  {
    "id": "32",
    "name": "Podgorica",
    "country": "Montenegro",
    "latitude_deg": "42.3594",
    "longitude_deg": "19.2519",
    "port_city": "0"
  },
  {
    "id": "33",
    "name": "Skopje",
    "country": "North Macedonia",
    "latitude_deg": "41.9616",
    "longitude_deg": "21.6214",
    "port_city": "0"
  },
  {
    "id": "34",
    "name": "Valletta",
    "country": "Malta",
    "latitude_deg": "35.8575",
    "longitude_deg": "14.4775",
    "port_city": "1"
  },
  {
    "id": "35",
    "name": "Amsterdam",
    "country": "Netherlands",
    "latitude_deg": "52.3086",
    "longitude_deg": "4.76389",
    "port_city": "1"
  },
  {
    "id": "36",
    "name": "Oslo",
    "country": "Norway",
    "latitude_deg": "60.1939",
    "longitude_deg": "11.1004",
    "port_city": "1"
  },
  {
    "id": "37",
    "name": "Warsaw",
    "country": "Poland",
    "latitude_deg": "52.1657",
    "longitude_deg": "20.9671",
    "port_city": "0"
  },
  {
    "id": "38",
    "name": "Lisbon",
    "country": "Portugal",
    "latitude_deg": "38.7813",
    "longitude_deg": "-9.13592",
    "port_city": "1"
  },
  {
    "id": "39",
    "name": "Bucharest",
    "country": "Romania",
    "latitude_deg": "44.5711",
    "longitude_deg": "26.085",
    "port_city": "0"
  },
  {
    "id": "40",
    "name": "Belgrade",
    "country": "Serbia",
    "latitude_deg": "44.8184",
    "longitude_deg": "20.3091",
    "port_city": "0"
  },
  {
    "id": "41",
    "name": "Stockholm",
    "country": "Sweden",
    "latitude_deg": "59.6519",
    "longitude_deg": "17.9186",
    "port_city": "1"
  },
  {
    "id": "42",
    "name": "Ljubljana",
    "country": "Slovenia",
    "latitude_deg": "46.2237",
    "longitude_deg": "14.4576",
    "port_city": "0"
  },
  {
    "id": "43",
    "name": "Bratislava",
    "country": "Slovakia",
    "latitude_deg": "48.1702",
    "longitude_deg": "17.2127",
    "port_city": "0"
  },
  {
    "id": "44",
    "name": "Domagnano",
    "country": "San Marino",
    "latitude_deg": "43.9489",
    "longitude_deg": "12.5114",
    "port_city": "0"
  },
  {
    "id": "45",
    "name": "Tunis",
    "country": "Tunisia",
    "latitude_deg": "36.851",
    "longitude_deg": "10.2272",
    "port_city": "1"
  },
  {
    "id": "46",
    "name": "Ankara",
    "country": "Turkey",
    "latitude_deg": "40.1281",
    "longitude_deg": "32.9951",
    "port_city": "0"
  },
  {
    "id": "47",
    "name": "Kiev",
    "country": "Ukraine",
    "latitude_deg": "50.345",
    "longitude_deg": "30.8947",
    "port_city": "0"
  },
  {
    "id": "48",
    "name": "Prishtina",
    "country": "Kosovo",
    "latitude_deg": "42.5728",
    "longitude_deg": "21.035",
    "port_city": "0"
  }
]
export {cityData};
