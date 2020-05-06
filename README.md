# CSV2XML

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Csv2Xml is a libary used to convert a CSV(comma-separated values) file to XML(extensible markup language).

  - Input as CSV file.
  - Get a Xml file
  - Magic !!

# Features!

  - Import a csv file as input.
  - Conversion of xml data from the csv

### Tech

Csv2xml uses a number of open source projects to work properly:

* [Pandas] - Pandas libary to parse the csv file.


### Installation

Csv2xml requires [Python 3](https://www.python.org/downloads/) v3+ to run.

Install the dependencies and start the server.

```sh
$ pip install Csv2Xml
```
### How to run
`from Csv2xml import Csv2Xml`
`Csv2Xml=Csv2Xml(filePath,root='Optional',children='Optional')`
`Csv2Xml.parse2Xml()`
### Output
`<Payload>
<tuple>
<Position>Business Analyst<Position/>
<Level>1<Level/>
<Salary>45000<Salary/>
</tuple>
<tuple>
<Position>Junior Consultant<Position/>
<Level>2<Level/>
<Salary>50000<Salary/>
</tuple>
<tuple>
<Position>Senior Consultant<Position/>
<Level>3<Level/>
<Salary>60000<Salary/>
</tuple>
<tuple>
<Position>Manager<Position/>
<Level>4<Level/>
<Salary>80000<Salary/>
</tuple>
<tuple>
<Position>Country Manager<Position/>
<Level>5<Level/>
<Salary>110000<Salary/>
</tuple>
<tuple>
<Position>Region Manager<Position/>
<Level>6<Level/>
<Salary>150000<Salary/>
</tuple>
<tuple>
<Position>Partner<Position/>
<Level>7<Level/>
<Salary>200000<Salary/>
</tuple>
<tuple>
<Position>Senior Partner<Position/>
<Level>8<Level/>
<Salary>300000<Salary/>
</tuple>
<tuple>
<Position>C-level<Position/>
<Level>9<Level/>
<Salary>500000<Salary/>
</tuple>
<tuple>
<Position>CEO<Position/>
<Level>10<Level/>
<Salary>1000000<Salary/>
</tuple></Payload>`
### Development

Want to contribute? Great!

Csv2xml uses pandas libary.
Make a change in your file and instantaneously see your updates!

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:5000
```


License
----

MIT

**Free Software, Hell Yeah!**


   
