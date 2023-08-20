# Wind Turbine with Azure Digital Twins and Azure Data Explorer 
## Architecture
- Data flow:
![Architecture](https://github.com/Anh-Dinh/Azure-Digital-Twin-in-Smart-City/blob/main/Data%20Flow.png)
## Component:
- Azure IoT Hub - Cloud Device and Security management, for receiving data from device sensor
- Azure Event Grid - Send telemetry to event grid subscription
- Azure Functions - using event grid trigger to read from Event Grid subscription and update accordingly to Azure Digital Twin
- Azure Digital Twins - Store Current data in Twin and Export to Event Hub
- Azure Event Hub - intermediate store to push to Azure Data Explorer
- Azure Data Explorer - historical data storage for further analytics
## Set Up:
Reference: https://learn.microsoft.com/en-us/azure/digital-twins/how-to-ingest-iot-hub-data
- Step 1: Set up Azure IoT Hub
  - 1: Create an Azure IoT Hub instance
  - 2: Create a device with a device id
  - 3: Make note of the device connection string and replace in the TurbinetoIoTHub.py
- Step 2: Azure Digital Twins
  - 1: Setup a digital twin instance
  - 2: Using the Windturbine.json model (DTDL language) to describe the properties, relationships, and capabilities of your device.
  - 3: Create a Twin with a matching twin id from thee  device id in IoT Hub
- Step 3: Set up the device sensor (Python)
  - 1: Install the required Python libraries: pip install azure-iot-device azure-iot-hub
  - 2: Running the TurbinetoIoTHub.py to send the data to Azure IoT Hub
- Step 4: Create Azure Function - C#
  - 1: Using Visual Studio to create a Azure Function project (follow the step in the reference link). Using the IoTHubtoTwins.cs code to paste in the main code file
  - 2: Configure the function app to connect to Azure Digital Twin
- Step 5: Connect the function to IoT Hub
  - 1: Create an event subscription that the IoT Hub will use to send event data to the IoTHubtoTwins function
  - 2: Running both TurbinetoIoTHub.py and Azure Function in the same time.
  - 3: Seeing updated data in Azure Digital Twins Explorer
    - Event Grid:
       ![Event Grid](https://github.com/Anh-Dinh/Azure-Digital-Twin-in-Smart-City/blob/main/images/Event%20Grid.png)
    - Azure Function:
      ![Azure Function](https://github.com/Anh-Dinh/Azure-Digital-Twin-in-Smart-City/blob/main/images/Function.png)
    - Azure Digital Twins Explorer Updated:
      ![Azure Digital Twins](https://github.com/Anh-Dinh/Azure-Digital-Twin-in-Smart-City/blob/main/images/Azure%20DT%20Data%20Explorer.png)
    
## Azure Digital Twins to Azure Data Explorer
Reference: https://learn.microsoft.com/en-us/azure/digital-twins/how-to-create-data-history-connection?tabs=portal
- Step 1: Create an Event Hub namespace and event hub
- Step 2: Create a Kusto (Azure Data Explorer) cluster and database
- Step 3: Set up data history connection between the Azure Digital Twins instance, the event hub, and the Azure Data Explorer cluster.
- Step 4: Verify the data flow
  - 1: Navigate to the event hub and Azure Digital Twins Explorer to ensure it's connected to the right instance.
    - Event Hub :
      ![Event Hub](https://github.com/Anh-Dinh/Azure-Digital-Twin-in-Smart-City/blob/main/images/EventHub.png)
    - Azure Digital Twins data visualization:
      ![Azure DT explorer](https://github.com/Anh-Dinh/Azure-Digital-Twin-in-Smart-City/blob/main/images/Azure%20Data%20Explorer%20Visualization.png)
    - Azure Data Explorer Dashboard:
      ![Azure Data Explorer](https://github.com/Anh-Dinh/Azure-Digital-Twin-in-Smart-City/blob/main/images/Azure%20Data%20Explorer.png)
    




