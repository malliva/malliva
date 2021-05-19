import { render } from '@testing-library/react';

import MarketAppTopMenu from './market-app-top-menu';

describe('MarketAppTopMenu', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppTopMenu />);
    expect(baseElement).toBeTruthy();
  });
});
