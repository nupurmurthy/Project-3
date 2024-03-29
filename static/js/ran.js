<div class="showcase__section" id="bubble">
  <div class="spacer --small"></div>
  <div id="bubbleplots">
    <div class="bubbleplot" data-num="0">
      <div class="plot" id="plotdiv"></div>
      <div class="control-row">
        Country: <select class="countrydata">
        </select>
      </div>
    </div>
  </div>
</div>
      
<script>
       Plotly.d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv', function(err, rows){

function unpack(rows, key) {
    return rows.map(function(row) { return row[key]; });
}

var allCountryNames = unpack(rows, 'country'),
allYear = unpack(rows, 'year'),
allGdp = unpack(rows, 'gdpPercap'),
listofCountries = [],
currentCountry,
currentGdp = [],
currentYear = [];

for (var i = 0; i < allCountryNames.length; i++ ){
if (listofCountries.indexOf(allCountryNames[i]) === -1 ){
  listofCountries.push(allCountryNames[i]);
}
}

function getCountryData(chosenCountry) {
currentGdp = [];
currentYear = [];
for (var i = 0 ; i < allCountryNames.length ; i++){
  if ( allCountryNames[i] === chosenCountry ) {
    currentGdp.push(allGdp[i]);
    currentYear.push(allYear[i]);
  } 
}
};

// Default Country Data
setBubblePlot('Afghanistan');

function setBubblePlot(chosenCountry) {
getCountryData(chosenCountry);  

var trace1 = {
  x: currentYear,
  y: currentGdp,
  mode: 'lines+markers',
  marker: {
    size: 12, 
    opacity: 0.5
  }
};

var data = [trace1];

var layout = {
  title: 'GDP per cap according to Country<br>'+ chosenCountry + ' GDP'
};

Plotly.newPlot('plotdiv', data, layout, {showSendToCloud: true});
};

var innerContainer = document.querySelector('[data-num="0"'),
plotEl = innerContainer.querySelector('.plot'),
countrySelector = innerContainer.querySelector('.countrydata');

function assignOptions(textArray, selector) {
for (var i = 0; i < textArray.length;  i++) {
  var currentOption = document.createElement('option');
  currentOption.text = textArray[i];
  selector.appendChild(currentOption);
}
}

assignOptions(listofCountries, countrySelector);

function updateCountry(){
setBubblePlot(countrySelector.value);
}

countrySelector.addEventListener('change', updateCountry, false);
});
        </script>
