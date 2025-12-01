import re

# file = open('test-input.txt')
file = open('input.txt')

seeds = []
soil = []
fertilizer = []
water = []
light = []
temperature = []
humidity = []
location = []
seedSoil = []
soilFertilizer = []
fertilizerWater = []
waterLight = []
lightTemperature = []
temperatureHumidity = []
humidityLocation = []
currDict = []

def SortMap(map, idx):
  map.sort(key=lambda map: map[idx])

def NextNums(old, new, map):
  oldMap = []
  for i in range(0, len(old), 2):
    oldMap.append([old[i], old[i+1]])
  SortMap(oldMap, 0)
  SortMap(map, 1)
  for om in oldMap:
    oldNum = om[0]
    oldRange = om[1]
    oComplete = False
    currNum = oldNum
    currRange = oldRange
    for m in map:
      if currNum < m[1]:
        new.append(currNum)
        newRange = min(currRange, m[0]-currNum)
        new.append(newRange)
        currNum += newRange
        currRange -= newRange
        if currRange == 0:
          oComplete = True
          break
      if currNum <= m[1]+m[2]:
        num = m[0]+currNum-m[1]
        new.append(num)
        newRange = min(currRange, m[2]+m[0]-num)
        new.append(newRange)
        currNum += newRange
        currRange -= newRange
        if currRange == 0:
          oComplete = True
          break
    if not oComplete:
      new.append(currNum)
      new.append(currRange)
#part 1
  # for o in old:
  #   foundMap = False
  #   for m in map:
  #     if o >= m[1] and o <= m[1]+m[2]:
  #       new.append(m[0]+o-m[1])
  #       foundMap = True
  #       break
  #   if not foundMap:
  #     new.append(o)

print('building dicts')
for line in file:
  line.rstrip()
  if 'seeds:' in line:
    seeds = [int(x) for x in line.split()[1:]]
  elif 'seed-to-soil' in line:
    currDict = seedSoil
  elif 'soil-to-fertilizer' in line:
    currDict = soilFertilizer
  elif 'fertilizer-to-water' in line:
    currDict = fertilizerWater
  elif 'water-to-light' in line:
    currDict = waterLight
  elif 'light-to-temperature' in line:
    currDict = lightTemperature
  elif 'temperature-to-humidity' in line:
    currDict = temperatureHumidity
  elif 'humidity-to-location' in line:
    currDict = humidityLocation
  else:
    nums = [int(x) for x in line.split()]
    if len(nums):
      currDict.append(nums)

# test = []
# NextNums([50,10,40,10],test,[[45,45,8],[53,53,5]])
# print(test)
print('calculating soil')
NextNums(seeds, soil, seedSoil)
print('calculating fertilizer')
NextNums(soil, fertilizer, soilFertilizer)
print('calculating water')
NextNums(fertilizer, water, fertilizerWater)
print('calculating light')
NextNums(water, light, waterLight)
print('calculating temperature')
NextNums(light, temperature, lightTemperature)
print('calculating humidity')
NextNums(temperature, humidity, temperatureHumidity)
print('calculating location')
NextNums(humidity, location, humidityLocation)
#part1 print(min(location))
print(location[0])
# print(seeds, soil, fertilizer, water, light, temperature, humidity, location)
# print(seeds, seedSoil, soilFertilizer, fertilizerWater, waterLight, lightTemperature, temperatureHumidity, humidityLocation)