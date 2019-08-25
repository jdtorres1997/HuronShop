var app = angular.module("HuronShopAngular", []);

app.config(function($interpolateProvider) { $interpolateProvider.startSymbol('{$'); $interpolateProvider.endSymbol('$}'); });

Fuente: https://www.iteramos.com/pregunta/7206/angularjs-con-django---conflicto-etiquetas-de-plantilla
app.controller("pedidos_controller", function ($scope) {
    $scope.nombre_prueba = "Prueba";
    $scope.form = {};
    $scope.mvtos_pedido = [];
    $scope.mvtos_eliminados_pedido = [];
    $scope.productos_list = [];
    $scope.precio_total = 0;

    $(document).ready(function () {
        console.log("Inicia controlador");
    });

    $scope.actualizar_total = function () {
        $scope.precio_total = 0;
        var total = 0;
        $scope.mvtos_pedido.forEach(function(element) {
            total += element['costo'] ? element['costo'] : 0;
        });
        $scope.precio_total = total;
    };

    $scope.prueba = function () {
        console.log("Entra");
        console.log($scope.mvtos_pedido);
    };

    $scope.init_productos = function (productos) {
        console.log("Entra a init", productos);
        $scope.productos_list = productos;
    };

    $scope.init_mvtos = function (mvtos) {
        console.log("Entra a init", mvtos);
        $scope.mvtos_pedido = mvtos;
        $scope.actualizar_total();
    };

    $scope.init_tallas = function(item) {
        console.log("Entra a iniciar tallas y precios", item);
        $scope.productos_list.forEach(function(element) {
            if (element['id'] == item['producto_id']){
                item['precio'] = element.precio;
                item['tallas'] = element.tallas;
            }
            console.log("Entra a asignar precio", item);
        });
    }

    $scope.addItem = function () {
        var mvto = {
            'id': 0,
            'producto_id': '',
            'cantidad': 0,
            'precio': 0,
            'costo': 0,
            'talla': '',
            'color': '',
            'tallas': [],
        };
        $scope.mvtos_pedido.push(mvto);
    }

    $scope.delItem = function(index, item) {
		if (typeof (item) !== 'undefined' && item.id !== 0 ) {
			$scope.mvtos_eliminados_pedido.push(item.id);
        }
        $scope.mvtos_pedido.splice(index, 1);
        $scope.actualizar_total();
    }
    
    $scope.asignarPrecio = function(item) {
        console.log("Entra a asignar precio", item);
        //item['talla'] = ''; //--Revisar, medio machetazo
        $scope.productos_list.forEach(function(element) {
            if (element['id'] == item['producto_id']){
                item['precio'] = element.precio;
                item['tallas'] = element.tallas;
            }
        });
    }
});