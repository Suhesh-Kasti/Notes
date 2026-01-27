---
category:
  - Networking
tags:
  - wireshark
published: false
date: 2024-08-15T07:49:00
excalidraw-plugin: parsed
excalidraw-open-md: true
---
We can filter a particular conversation using  "Conversation filter".

## Profiles
- Specific profiles for each type of work that needs to be performed 
- Useful if we want to use one configuration for one type of analysis and another type of configuration for another type of analysis

Time can be adjusted using the view tab. One of the useful way to display time can be *Seconds since previous displayed packet*. This can be used to find packet delays.

#### 1. Adding an extra time column
> Edit > Preferences > Columns > Add
#### 2. Saving filters for future
> + icon on top right > Add name and filter > Save
#### 3. Adjusting colors
Let's color all TCP SYN packets
`tcp.flags.syn==1`
> View > Coloring rules > Add 
The list will be in order of priority ie. 1st highest priority, 2nd - less priority

NOTE: If we ever need to figure out a filter command we can select the required option and wireshark will display the filter on bottom left 
![[wireshark_knowcommand.png]]

#### 4. Change layout 
> Edit > Preferences > Layouts
#### 5. Add values as column 
> Right on the value > Add as column
> We can also remove any column temporarily by clicking on the columns



%%
# Excalidraw Data
## Text Elements
## Drawing
```compressed-json
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=
```
%%