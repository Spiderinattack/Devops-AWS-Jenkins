.mode csv

CREATE temp TABLE [order_delta](
   [OrderID]INTEGER ,
   [CustomerID]TEXT,
   [EmployeeID]INTEGER,
   [OrderDate]DATETIME,
   [RequiredDate]DATETIME,
   [ShippedDate]DATETIME,
   [ShipVia]INTEGER,
   [Freight]NUMERIC DEFAULT 0,
   [ShipName]TEXT,
   [ShipAddress]TEXT,
   [ShipCity]TEXT,
   [ShipRegion]TEXT,
   [ShipPostalCode]TEXT,
   [ShipCountry]TEXT
);

.import PyUnit/order_delta.csv order_delta

insert into fact_order
select 
o.OrderID,
o.CustomerID,
c.ContactName,
c.Phone,
o.EmployeeID,
e.FirstName,
e.LastName,
o.OrderDate,
o.RequiredDate,
o.ShippedDate,
o.ShipVia,
t.TerritoryDescription,
o.Freight,
o.ShipName,
o.ShipAddress,
o.ShipCity,
o.ShipRegion,
o.ShipPostalCode,
o.ShipCountry 
from order_delta o 
left join employees e on o.employeeid=e.employeeid
left join customers c on o.customerid=c.customerid
left join territories t on  o.shipvia=t.TerritoryID;
