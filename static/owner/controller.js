var app = angular.module("HuronShopAngular", []);

app.controller("pedidos_controller", function ($scope) {
    $scope.nombre_prueba = "Prueba";
    $scope.form = {};

    $(document).ready(function () {
        console.log($scope);
    });

    $scope.prueba = function () {
        console.log("Entra");
        console.log($scope.nombre_prueba);
        console.log($scope);
    };
});