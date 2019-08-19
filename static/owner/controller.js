var app = angular.module("HuronShopAngular", []);

app.controller("pedidos_controller", function ($scope) {
    $scope.nombre_prueba = "Prueba";

    $scope.prueba = function () {
        console.log("Entra");
    };
});