module.exports = function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({
      data: ' response from the API',
    });
  }
};