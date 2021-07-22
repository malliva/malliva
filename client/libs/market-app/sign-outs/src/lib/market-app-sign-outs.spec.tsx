import { render } from '@testing-library/react';

import MarketAppSignOuts from './market-app-sign-outs';

describe('MarketAppSignOuts', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppSignOuts />);
    expect(baseElement).toBeTruthy();
  });
});
