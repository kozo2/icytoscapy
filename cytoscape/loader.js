if (window['cytoscape'] === undefined) {

    var paths = {
        cytoscape: 'http://cytoscape.github.io/cytoscape.js/api/cytoscape.js-latest/cytoscape.min'
    };

    require.config({
        paths: paths
    });


    require(['cytoscape'], function(cytoscape) {
        // // window['arbor'] = arbor;
        // // window['cytoscape'] = cytoscape;

        // var event = document.createEvent("HTMLEvents");
        // event.initEvent("load_cytoscape", true, false);
        // window.dispatchEvent(event);

        return {
            cytoscape: cytoscape
        };
    });
}