This example pulls together various examples of work with trees in D3.js.

The panning functionality can certainly be improved in my opinion and I would be thrilled to see better solutions contributed.

One can do all manner of housekeeping or server related calls on the drop event to manage a remote tree dataset for example.

Dragging can be performed on any node other than root (flare).
Dropping can be done on any node.

Panning can either be done by dragging an empty part of the SVG around or dragging a node towards an edge.

Zooming is performed by either double clicking on an empty part of the SVG or by scrolling the mouse-wheel.
To Zoom out hold shift when double-clicking.

Expanding and collapsing of nodes is achieved by clicking on the desired node.

The tree auto-calculates its sizes both horizontally and vertically so it can adapt between many nodes being present in the view to very few whilst making the view managable and pleasing on the eye.

For any help/queries, http://www.robschmuecker.com @robschmuecker or robert.schmuecker at gmail dot com