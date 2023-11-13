import handleResponseFromAPI from "./2-then";

test("handleResponseFromAPI return the right response on resolve", () => {
  const promise = Promise.resolve();

  const successResponse = handleResponseFromAPI(promise);
  return expect(successResponse).resolves.toEqual({
    body: 'success',
    status: 200
  });
});
