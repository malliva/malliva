import { render } from '@testing-library/react';

import MarketAppMainFilter from './market-app-main-filter';

describe('MarketAppMainFilter', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppMainFilter />);
    expect(baseElement).toBeTruthy();
  });
});
