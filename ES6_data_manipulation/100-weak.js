export const weakMap = new WeakMap();
export function queryAPI(endpoint) {
  const endpointCount = weakMap.has(endpoint)
    ? weakMap.get(endpoint)
    : 0;
  const newEndpointCount = endpointCount + 1;

  if (newEndpointCount >= 5) {
    throw new Error('Endpoint load is high');
  }

  weakMap.set(endpoint, newEndpointCount);
}
