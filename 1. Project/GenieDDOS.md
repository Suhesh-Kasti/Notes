---
category:
  - Networking
tags:
  - genie
published: false
date: 2024-07-11T12:20:00.000Z
excalidraw-plugin: parsed
excalidraw-open-md: true
---

Provides network operators the functionality to **analyze traffic** and **mitigate** DDoS attacks.
- Allows users to **monitor** and **analyze** network traffic, and generate **traffic reports**.
![[genieArchitechture.png]]
#### **System Overview**
Components: Controller, Collector, Network Traffic Modeling.
1. **Collector**: 
   - Managing configuration and generating reports.
   - Connects to [[BGP(Border Gateway Protocol)]] routers to collect flow records.
2. **Controller**: 
   - Aggregates collected data into a database; uses CLI for configuration.
   - Collecting flows and sending classified data to controller.
   -  As a controller takes data from collector and aggregates it into a database.
# **Steps**
1. **Licensing and Verification**: Ensure controller and collector licenses are enabled.
2. **IP Configuration**:
   - Assign IP addresses to interfaces.
   - Create SNMP community string (`snmp-server community ‘string’ RO or RW`).
   - Configure IP route (`ip route 0.0.0.0 0.0.0.0 192.168.x.x 0`).
   - Set hostname if required.
   - Configure management IP (`module local ip 192.168.x.x`).

3. **Additional Configuration**:
   - Set IP addresses for DNS (`ip name-server 192.168.x.x`) and NTP server (`ntp server 192.168.x.x`).
   - Configure controller (`remote controller ip 192.168.x.x priority 1`) and its ID.
   - Configure collector with its ID and permissions.

4. **Database Configuration**:
   - Use internal storage (`db use internal`).
   - Initialize database (`run db init internet`).
   - Save configurations and reload system (`write config` and `reload now`).
#### **3. Configuration Overview**

**Login Portal**:
- **Default Credentials**:
  - UI: `admin/admin@atm`
  - CLI: `genie/genieatm`
- **URLs**:
  - GA dashboard: `http://192.168.180.6/default#`
  - GA admin: `http://192.168.180.6:8443`

**Configuring Controller**:
- Navigate: `System admin > Analyzer > Controller`
- Verify SNMP settings using SNMPWALK.

**Configuring Collector**:
- Navigate: `System admin > Analyzer > Controller`
- Ensure BGP routers are configured before adding BGP connections.

**Configuring Router**:
- Navigate: `System admin > Device > Router`
- Provide router name, select collector, and configure SNMP and NetFlow.

**Configuring Interfaces**:
- Add router interfaces using SNMP discovery and assign boundaries.

**Configuring Subnetwork**:
- Navigate: `System admin > Network > Sub-Network`
- Fill in sub-network details and set default configurations.
#### **4. Anomaly Detection and Notification**

**Configuration**:
- **Report**: Define network scope and add AS details.
- **Boundaries**: Configure major and secondary boundaries.
- **Top-N Report**: Aggregate traffic data for anomaly detection.

**Anomaly Detection**:
- Set baseline thresholds.
- Enable host-based and prefix-based DDoS anomaly detection.

**Anomaly Notification**:
- Enable email notifications and configure recipients.

**Adding Routers**:
- Navigate: `System admin > Analyzer > Collector`
- Add collector IP as BGP identifier and configure routers.
#### **5. Configuring Mitigation**

**Configuring BGP Peer**:
- Add BGP peer (redirection router) between mitigation device and GenieATM.
- Enter router details and verify AS numbers.

**Configuring Mitigation Device**:
- Add and configure third-party mitigation devices (e.g., F5).

**Configuring SNMP**:
- Ensure SNMP settings are configured on mitigation devices.
- Verify using SNMPWALK.

**Redirection Routers**:
- Add injection router to handle cleaned traffic from mitigation device.

**Mitigation Fail-Safe**:
- Enable device status checks to ensure mitigation devices are operational.

**Existing Zones**:
- Update virtual server configurations using SNMP polling.

**Configuring Protection Profile**:
- Edit or create protection profiles for DDoS detection.
- Configure attack vectors, thresholds, and detection settings.

**Configuring Policy Template**:
- Create policies for mitigation with specific protection profiles.
- Define criteria to trigger mitigation based on severity and attack type.

**Protected Zone**:
- Configure auto-mitigation settings and define network scope.
#### **6. DDoS Detection and Mitigation Mechanisms**

**Fast Detection**:
- Per router, per host-based detection.
- Triggers anomaly if traffic exceeds baseline value.

**Accumulative Detection**:
- Analyzes total attack traffic across multiple routes.
- Detects anomalies for all layer 3, 4, 7, and DNS/SIP attacks.

**Mitigation Process**:
- Redirects attack traffic to F5 BIG-IP for cleaning.
- Re-injects cleaned traffic back to customer network.

**Examples and Additional Notes**:

- **SNMPWALK**: Used to verify SNMP configurations.
- **Baseline Thresholds**: Customizable for different types of traffic anomalies.
- **Email Notifications**: Ensure timely alerts for detected anomalies.

%%
## Drawing
```compressed-json
N4IgLgngDgpiBcIYA8DGBDANgSwCYCd0B3EAGhADcZ8BnbAewDsEAmcm+gV31TkQAswYKDXgB6MQHNsYfpwBGAOlT0AtmIBeNCtlQbs6RmPry6uA4wC0KDDgLFLUTJ2lH8MTDHQ0YNMWHRJMRZFEIAOMiRPVRhGMBoEAG0AXXJ0KCgAZQCwPlBJfDxM7A0+Rk5MTHIdGCIAIXRUAGsCrkZcAGF6THp8BBAAYgAzEdGQAF9xoA===
```
%%
